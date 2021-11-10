from enum import Enum
import xml.etree.ElementTree as ET

from solargis.abstractelement import AbstractElement
from solargis.validator import Validator


class EfficiencyType(Enum):
     """Concrete type of how efficiency of the inverter should be modeled"""
     EfficiencyConstant = 'pv:EfficiencyConstant'
     EfficiencyCurve = 'pv:EfficiencyCurve'


class Inverter(AbstractElement):

    def __init__(self, efficiency=None, limitation_ac: float = None):

        self.efficiency = efficiency
        self.limitation_ac = limitation_ac

        self.prefix = 'pv'
        self.element_name = 'inverter'

    def to_element(self):
        if self.efficiency is None and self.limitation_ac is None:
            return None

        inverter = ET.Element(self.get_element_name())

        if self.efficiency is not None:
            if type(self.efficiency) in (float, int):
                attributes = {
                    'xsi:type': EfficiencyType.EfficiencyConstant.value,
                    'percent': str(self.efficiency),
                }
            else:
                attributes  = {
                    'xsi:type': EfficiencyType.EfficiencyCurve.value,
                    'dataPairs': self.efficiency,
                }
            ET.SubElement(inverter, 'pv:efficiency', attrib=attributes)

        if self.limitation_ac is not None:
            limitation_ac = ET.SubElement(inverter, 'pv:limitationACPower')
            limitation_ac.text = str(self.limitation_ac)

        return inverter
