from enum import Enum
from solargis.abstractelement import AbstractElement
from solargis.validator import Validator
import xml.etree.ElementTree as ET

class GeometryXsiType(Enum):
    GeometryFixedOneAngle = 'pv:GeometryFixedOneAngle'


class Geometry(AbstractElement):
    """	Parametrization of PV system mounting type used for
    calculating GTI and PVOUT. If this element is missing and
    GTI/PVOUT is requested, flat-lying PV panels are considered
    (GTI=GHI)
    """
    def __init__(self, xsi_type: GeometryXsiType, azimuth: float, tilt: float):
        self.prefix = 'pv'
        self.element_name = 'geometry'

        Validator.value_in_enum(xsi_type, GeometryXsiType)

        self.xsi_type = xsi_type
        self.azimuth = azimuth
        self.tilt = tilt

    def to_element(self):
        attributes = dict()
        attributes['xsi:type'] = self.xsi_type.value
        attributes['azimuth'] = str(self.azimuth)
        attributes['tilt'] = str(self.tilt)
        return ET.Element(self.get_element_name(), attrib=attributes)
