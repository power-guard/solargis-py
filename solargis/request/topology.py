import xml.etree.ElementTree as ET
from enum import Enum

from solargis.abstractelement import AbstractElement
from solargis.validator import Validator


class TopologyXsiType(Enum):
    TopologySimple = 'pv:TopologySimple'
    TopologyRow = 'pv:TopologyRow'
    GeometryFixedOneAngle = 'pv:GeometryFixedOneAngle'
    TopologyColumn = 'pv:TopologyColumn'

class MagnitudeType(Enum):
    PROPORTIONAL = 'PROPORTIONAL'
    UNPROPORTIONAL1 = 'UNPROPORTIONAL1'
    UNPROPORTIONAL2 = 'UNPROPORTIONAL2'
    UNPROPORTIONAL3 = 'UNPROPORTIONAL3'

class Topology(AbstractElement):
    def __init__(self, xsi_type: TopologyXsiType, relative_spacing: float,
        magnitude_of_loss: MagnitudeType = None):

        Validator.value_in_enum(xsi_type, TopologyXsiType)
        if magnitude_of_loss is not None:
            Validator.value_in_enum(magnitude_of_loss, MagnitudeType)

        self.xsi_type = xsi_type
        self.relative_spacing = relative_spacing
        self.magnitude_of_loss = magnitude_of_loss

        self.prefix = 'pv'
        self.element_name = 'topology'

    def to_element(self):
        attributes = dict()
        attributes['xsi:type'] = self.xsi_type.value
        attributes['relativeSpacing'] = str(self.relative_spacing)

        if self.magnitude_of_loss is not None:
            attributes['type'] = self.magnitude_of_loss.value

        return ET.Element(self.get_element_name(), attrib=attributes)
