import unittest

from solargis.request import Terrain

class TestLosses(unittest.TestCase):


    def test_terrain_element_empty(self):
        terrain = Terrain()
        element = terrain.to_element()
        self.assertIsNone(element)

    def test_terrain_element_with_elevation(self):
        terrain = Terrain(elevation=5.4)
        expected = '<geo:terrain elevation="5.4" />'
        actual = terrain.to_xml()
        self.assertEqual(actual, expected)

    def test_terrain_element_with_all(self):
        terrain = Terrain(elevation=1.0, azimuth=90, tilt=45.0)
        expected = '<geo:terrain elevation="1.0" azimuth="90" tilt="45.0" />'
        actual = terrain.to_xml()
        self.assertEqual(actual, expected)
