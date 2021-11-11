import unittest

from solargis.request import Geometry, GeometryXsiType

class TestGeometry(unittest.TestCase):

    def test_geometry_element(self):
        geometry = Geometry(
            GeometryXsiType.GeometryFixedOneAngle,
            azimuth=205,
            tilt=18
        )
        expected = '<pv:geometry xsi:type="pv:GeometryFixedOneAngle" azimuth="205" tilt="18" />'
        actual = geometry.to_xml()
        self.assertEqual(actual, expected)
