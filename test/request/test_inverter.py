import unittest

from solargis.request import Inverter

class TestInverter(unittest.TestCase):

    def test_inverter_element_none(self):
        inverter = Inverter(None, None)
        element = inverter.to_element()
        self.assertIsNone(element)

    def test_inverter_element_efficiency_constant(self):
        inverter = Inverter(98, 1715)
        expected = (
            '<pv:inverter>'
            '<pv:efficiency xsi:type="pv:EfficiencyConstant" percent="98" />'
            '<pv:limitationACPower>1715</pv:limitationACPower>'
            '</pv:inverter>'
        )
        actual = inverter.to_xml()
        self.assertEqual(actual, expected)

    def test_inverter_element_efficiency_curve(self):
        efficiency = '0:20 50:60 100:80'
        inverter = Inverter(efficiency, 1715)
        expected = (
            '<pv:inverter>'
            '<pv:efficiency xsi:type="pv:EfficiencyCurve" dataPairs="0:20 50:60 100:80" />'
            '<pv:limitationACPower>1715</pv:limitationACPower>'
            '</pv:inverter>'
        )
        actual = inverter.to_xml()
        self.assertEqual(actual, expected)
