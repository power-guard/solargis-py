import xml.etree.ElementTree as ET

from solargis.abstractelement import AbstractElement
from solargis.validator import Validator


class Terrain(AbstractElement):
    def __init__(self, elevation: float = None, azimuth: float = None,
        tilt: float = None):

        if azimuth is not None:
            # 0 is north. 180 is south
            Validator.value_in_range(azimuth, 0, 360, 'azimuth')
        if tilt is not None:
            Validator.value_in_range(tilt, 0, 90, 'tilt')

        self.elevation = elevation
        self.azimuth = azimuth
        self.tilt = tilt

        self.element_name = 'terrain'
        self.prefix = 'geo'

    def to_element(self):
        if self.elevation is None and \
            self.azimuth is None and \
            self.tilt is None:
            return None

        attributes = dict()
        if self.elevation is not None:
            attributes['elevation'] = str(self.elevation)
        if self.azimuth is not None:
            attributes['azimuth'] = str(self.azimuth)
        if self.tilt is not None:
            attributes['tilt'] = str(self.tilt)

        return ET.Element(self.get_element_name(), attrib=attributes)
