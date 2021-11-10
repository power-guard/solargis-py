import unittest

from solargis.request import AcLosses, DcLosses, Losses

class TestLosses(unittest.TestCase):

    def test_losses_element_empty(self):
        ac = AcLosses(None, None)
        dc = DcLosses(None, None, None)
        losses = Losses(ac, dc)
        element = losses.to_element()
        self.assertIsNone(element)

    def test_losses_element(self):
        ac = AcLosses(1.0, 2.0)
        dc = DcLosses(2.5, 2.0, 1.0)
        losses = Losses(ac, dc)

        ac_txt = '<pv:acLosses transformer="1.0" cables="2.0" />'
        dc_txt = '<pv:dcLosses snowPollution="2.5" cables="2.0" mismatch="1.0" />'
        expected = '<pv:losses>' + ac_txt + dc_txt + '</pv:losses>'
        actual = losses.to_xml()
        self.assertEqual(actual, expected)

    def test_losses_element_prefix(self):
        ac = AcLosses(1.0, 2.0)
        dc = DcLosses(2.5, 2.0, 1.0)
        losses = Losses(ac, dc)

        ac_txt = '<pv:acLosses transformer="1.0" cables="2.0" />'
        dc_txt = '<pv:dcLosses snowPollution="2.5" cables="2.0" mismatch="1.0" />'
        expected = '<pv:losses>' + ac_txt + dc_txt + '</pv:losses>'
        actual = losses.to_xml()
        self.assertEqual(actual, expected)

    def test_aclosses_element_empty(self):
        ac_losses = AcLosses(None, None)
        element = ac_losses.to_element()
        self.assertIsNone(element)

    def test_aclosses_element(self):
        ac_losses = AcLosses(1.0, 2.0)

        expected = '<pv:acLosses transformer="1.0" cables="2.0" />'
        actual = ac_losses.to_xml()
        self.assertEqual(actual, expected)

    def test_dclosses_element_empty(self):
        dc_losses = DcLosses(None, None, None, None)
        element = dc_losses.to_element()
        self.assertIsNone(element)

    def test_dclosses_element(self):
        dc_losses = DcLosses(2.5, 2.0, 1.0)

        expected = '<pv:dcLosses snowPollution="2.5" cables="2.0" mismatch="1.0" />'
        actual = dc_losses.to_xml()
        self.assertEqual(actual, expected)

    def test_dclosses_monthly_snow_pollution(self):
        dc_losses = DcLosses(2.5, 2.0, 1.0, '5 5.2 3 1 1 1 1 1 1 1 2 4')

        expected = '<pv:dcLosses monthlySnowPollution="5 5.2 3 1 1 1 1 1 1 1 2 4" cables="2.0" mismatch="1.0" />'
        actual = dc_losses.to_xml()
        self.assertEqual(actual, expected)
