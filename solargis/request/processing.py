from enum import Enum
import xml.etree.ElementTree as ET

from solargis.abstractelement import AbstractElement
from solargis.validator import Validator

class Summarization(Enum):
    YEARLY = 'YEARLY'
    MONTHLY = 'MONTHLY'
    DAILY = 'DAILY'
    HOURLY = 'HOURLY'
    MIN_30 = 'MIN_30'
    MIN_15 = 'MIN_15'
    MIN_10 = 'MIN_10'
    MIN_5 = 'MIN_5'

class Key(Enum):
    GHI = 'GHI'                       # Global Horizontal Irradiation [kWh/m2, Wh/m2 resp. W/m2]
    GHI_C = 'GHI_C'                   # Clear-sky Global Horizontal Irradiation [kWh/m2, Wh/m2 resp. W/m2]
    GHI_UNC_HIGH = 'GHI_UNC_HIGH'     # GHI high estimate (10 % prob. of exceedance) [kWh/m2, Wh/m2 resp. W/m2]
    GHI_UNC_LOW = 'GHI_UNC_LOW'       # GHI low estimate (90 % prob. of exceedance) [kWh/m2, Wh/m2 resp. W/m2]
    DNI = 'DNI'                       # Direct Normal Irradiation [kWh/m2, Wh/m2 resp. W/m2]
    DNI_C = 'DNI_C'                   # Clear-sky Direct Normal Irradiation [kWh/m2, Wh/m2 resp. W/m2]
    DIF = 'DIF'                       # Diffuse Horizontal Irradiation [kWh/m2, Wh/m2 resp. W/m2]
    GTI = 'GTI'                       # Global Tilted Irradiation [kWh/m2, Wh/m2 resp. W/m2]
    GTI_UNC_HIGH = 'GTI_UNC_HIGH'     # GTI high estimate (10 % prob. of exceedance) [kWh/m2, Wh/m2 resp. W/m2]
    GTI_UNC_LOW = 'GTI_UNC_LOW'       # GTI low estimate (90 % prob. of exceedance) [kWh/m2, Wh/m2 resp. W/m2]
    GTI_C = 'GTI_C'                   # Global tilted clear-sky irradiance [W/m2]
    CI_FLAG = 'CI_FLAG'               # Cloud identification quality flag [categories], this parameter is presented as 'flagR' in the response
    FLAG_R = 'FLAG_R'                 # alias for CI_FLAG
    KTM = 'KTM'                       # Deprecated alias of KC. Can be discontinued in future versions.
    KC = 'KC'                         # Clear-sky index [unitless]
    KT = 'KT'                         # clearness index, values range (0, 1.1), during the night -9
    PAR = 'PAR'                       # Photo-synthetically Active Irradiation [kWh/m2, Wh/m2 resp. W/m2]
    SE = 'SE'                         # Sun Altitude (Elevation) Angle [deg.]
    SA = 'SA'                         # Sun Azimuth Angle [deg.]
    TEMP = 'TEMP'                     # Air Temperature at 2m [deg. C]
    TD = 'TD'                         # Dew Point Temperature [deg. C]
    WBT = 'WBT'                       # Wet Bulb Temperature [deg. C]
    AP = 'AP'                         # Atmospheric Pressure [hPa]
    RH = 'RH'                         # Relative Humidity [%]
    WS = 'WS'                         # Wind Speed [m/s]
    WD = 'WD'                         # Wind Direction [deg.]
    PREC = 'PREC'                     # Precipitation Rate [kg/m2]
    PWAT = 'PWAT'                     # Precipitable Water [kg/m2]
    PVOUT = 'PVOUT'                   # Photovoltaic Output [kW, resp. kWh]
    PVOUT_UNC_HIGH = 'PVOUT_UNC_HIGH' # PVOUT high estimate (10 % prob. of exceedance) [kW, resp. kWh]
    PVOUT_UNC_LOW = 'PVOUT_UNC_LOW'   # PVOUT low estimate (90 % prob. of exceedance) [kW, resp. kWh]
    SDWE = 'SDWE'                     # Water equivalent of accumulated snow depth [kg/m2]
    SWE = 'SWE'                       # Deprecated alias of SDWE. Can be discontinued in future versions. SDWE will be returned in a response.
    TMOD = 'TMOD'                     # Module temperature [deg. C]. This parameter needs a PV system defined in the request.
    WG = 'WG'                         # Wind Gust [m/s]
    WS100 = 'WS100'                   # Wind speed at 100 m [m/s]
    WD100 = 'WD100'                   # Wind direction at 100 m [deg.]
    SFWE = 'SFWE'                     # Water equivalent of fresh snowfall rate [kg/m2/hour] - source ERA5 , the latest data available is approx. one month backward (no data for very recent or forecast period)
    INC = 'INC'                       # Incidence angle of direct irradiance [deg.], this parameter needs GTI or PVOUT in the request
    TILT = 'TILT'                     # Tilt of inclined surface [deg.], this parameter needs GTI or PVOUT in the request
    ASPECT = 'ASPECT'                 # Aspect of inclined surface [deg.], this parameter needs GTI or PVOUT in the request


class TimestampType(Enum):
    '''Valid for [sub]hourly summarization. Intervals can be
    time-stamped at the center (default) or at start or at end.'''

    START = 'START'
    CENTER = 'CENTER'
    END = 'END'


class Processing(AbstractElement):
    def __init__(self, summarization: Summarization, key: str,
        time_zone: str = None, timestamp_type: TimestampType = None,
        terrain_shading: bool = False):

        Validator.value_in_enum(summarization, Summarization)
        Validator.str_not_none_or_blank(key, 'key')

        if time_zone is not None:
            Validator.gmt_timezone(time_zone)

        if timestamp_type is not None:
            Validator.value_in_enum(timestamp_type, TimestampType)

        self.summarization = summarization
        self.key = key
        self.time_zone = time_zone
        self.timestamp_type = timestamp_type
        self.terrain_shading = terrain_shading

        self.element_name = 'processing'
        self.prefix = ''

    def to_element(self) -> ET.Element:
        attributes = dict()
        attributes['summarization'] = self.summarization.value
        attributes['key'] = self.key

        if self.terrain_shading:
            attributes['terrainShading'] = str(self.terrain_shading).lower()

        element = ET.Element(self.get_element_name(), attrib=attributes)

        if self.time_zone is not None:
            tz = ET.SubElement(element, 'timeZone')
            tz.text = self.time_zone

        if self.timestamp_type is not None:
            tst = ET.SubElement(element, 'timestampType')
            tst.text = self.timestamp_type.value

        return element
