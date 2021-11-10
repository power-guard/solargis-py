import unittest

from solargis.request import Topology, XsiType, MagnitudeType

class TestLosses(unittest.TestCase):


    def test_topology_element(self):
        topology = Topology(XsiType.TopologyRow, 1.5, MagnitudeType.UNPROPORTIONAL_1)
        expected = '<pv:topology xsi:type="pv:TopologyRow" relativeSpacing="1.5" type="UNPROPORTIONAL_1" />'
        actual = topology.to_xml()
        self.assertEqual(expected, actual)

