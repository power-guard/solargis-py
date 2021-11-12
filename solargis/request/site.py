import xml.etree.ElementTree as ET

from solargis.abstractelement import AbstractElement
from solargis.validator import Validator


class Site(AbstractElement):
    def __init__(self, id: str, latitude: float, longitude: float,
        name: str = None, geometry=None, system=None,
        terrain=None, horizon: str = None):

        Validator.str_not_none_or_blank(id, 'id')
        Validator.value_in_range(latitude, -90, 90, 'latitude')
        Validator.value_in_range(longitude, -180, 180, 'longitude')

        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.geometry = geometry
        self.system = system
        self.terrain = terrain
        self.horizon = horizon

        self.element_name = 'site'
        self.prefix = ''

    def to_element(self):
        attributes = dict()
        attributes['id'] = self.id
        attributes['lat'] = str(self.latitude)
        attributes['lng'] = str(self.longitude)

        if self.name:
            attributes['name'] = self.name

        element = ET.Element(self.get_element_name(), attrib=attributes)

        if self.geometry is not None:
            geometry = self.geometry.to_element()
            if geometry is not None:
                element.append(geometry)

        if self.system is not None:
            system = self.system.to_element()
            if system is not None:
                element.append(system)

        if self.terrain is not None:
            terrain = self.terrain.to_element()
            if terrain is not None:
                element.append(terrain)

        if self.horizon:
            horizon = ET.SubElement(element, 'geo:horizon')
            horizon.text = self.horizon

        return element
