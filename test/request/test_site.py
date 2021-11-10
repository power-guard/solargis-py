import unittest

from solargis.request import Site

class TestLosses(unittest.TestCase):


    def test_site_element_empty(self):
        site = Site('site_id', 42.0, 140.0)

        expected = '<site id="site_id" lat="42.0" lng="140.0" />'
        actual = site.to_xml()
        self.assertEqual(actual, expected)
