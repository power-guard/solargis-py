from enum import Enum
import xml.etree.ElementTree as ET

from solargis.abstractelement import AbstractElement
from solargis.validator import Validator


class ModuleType(Enum):
    CSI = 'CSI' # crystalline silicon
    ASI = 'ASI' # amorphous silicon
    CDTE = 'CDTE' # cadmium telluride,
    CIS = 'CIS' # copper indium selenide


class Module(AbstractElement):

    def __init__(self,
                 module_type: ModuleType,
                 degradation: float = None,
                 degradation_first_year: float = None,
                 nominal_operating_cell_temp: float = None,
                 pmax_coeff: float = None):

        Validator.value_in_enum(module_type, ModuleType)

        if degradation is not None:
            Validator.value_in_range(degradation, 0, 100, 'degradation')
        if degradation_first_year is not None:
            Validator.value_in_range(degradation_first_year, 0, 100, 'degradation first year')

        self.module_type = module_type
        self.degradation= degradation
        self.degradation_first_year= degradation_first_year
        self.nominal_operating_cell_temp= nominal_operating_cell_temp
        self.pmax_coeff= pmax_coeff

        self.element_name = 'module'
        self.prefix = 'pv'


    def to_element(self):
        attributes = dict()
        attributes['type'] = self.module_type.value

        module = ET.Element(self.get_element_name(), attrib=attributes)

        if self.degradation is not None:
            degradation = ET.SubElement(module, 'pv:degradation')
            degradation.text = str(self.degradation)

        if self.degradation_first_year is not None:
            degradation_first_year = ET.SubElement(module, 'pv:degradationFirstYear')
            degradation_first_year.text = str(self.degradation_first_year)

        if self.nominal_operating_cell_temp is not None:
            nominal_operating_cell_temp = ET.SubElement(module, 'pv:nominalOperatingCellTemp')
            nominal_operating_cell_temp.text = str(self.nominal_operating_cell_temp)

        if self.pmax_coeff is not None:
            pmax_coeff = ET.SubElement(module, 'pv:PmaxCoeff')
            pmax_coeff.text = str(self.pmax_coeff)

        return module
