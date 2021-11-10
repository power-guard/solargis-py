import unittest

from solargis.request import Module, ModuleType

class TestModule(unittest.TestCase):

    def test_module_element(self):
        module = Module(ModuleType.CSI, 0, 0.8, 45, -0.38)

        expected = (
            '<pv:module type="CSI">'
            '<pv:degradation>0</pv:degradation>'
            '<pv:degradationFirstYear>0.8</pv:degradationFirstYear>'
            '<pv:nominalOperatingCellTemp>45</pv:nominalOperatingCellTemp>'
            '<pv:PmaxCoeff>-0.38</pv:PmaxCoeff>'
            '</pv:module>'
        )
        actual = module.to_xml()
        self.assertEqual(actual, expected)

    def test_module_element_degradation(self):
        module = Module(ModuleType.CSI, 0.5)

        expected = (
            '<pv:module type="CSI">'
            '<pv:degradation>0.5</pv:degradation>'
            '</pv:module>'
        )
        actual = module.to_xml()
        self.assertEqual(actual, expected)

    def test_module_nominal_operating_cell_temp(self):
        module = Module(ModuleType.CSI, nominal_operating_cell_temp=45)

        expected = (
            '<pv:module type="CSI">'
            '<pv:nominalOperatingCellTemp>45</pv:nominalOperatingCellTemp>'
            '</pv:module>'
        )
        actual = module.to_xml()
        self.assertEqual(actual, expected)
