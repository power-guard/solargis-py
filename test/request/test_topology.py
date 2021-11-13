import unittest

from solargis.request import MagnitudeType, Topology, TopologyXsiType


class TestLosses(unittest.TestCase):

    def test_topology_element(self):
        topology = Topology(TopologyXsiType.TopologyRow, 1.5, MagnitudeType.UNPROPORTIONAL1)
        expected = '<pv:topology xsi:type="pv:TopologyRow" relativeSpacing="1.5" type="UNPROPORTIONAL1" />'
        actual = topology.to_xml()
        self.assertEqual(expected, actual)
