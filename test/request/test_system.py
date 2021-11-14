import datetime as dt
import unittest

from solargis.request import (AcLosses, DcLosses, InstallationType, Inverter,
                              Losses, Module, ModuleType, System)


class TestSystem(unittest.TestCase):

    def test_system_simple(self):
        module = Module(ModuleType.CSI)
        inverter = Inverter(efficiency=98)
        dc_losses = DcLosses(2.5, 4, 1)
        ac_losses = AcLosses(1.5, 1)
        losses = Losses(ac_losses, dc_losses)

        system = System(2310, module, inverter, losses,
            installation_type=InstallationType.FREE_STANDING,
            date_startup=dt.date(2018, 12, 24), self_shading=True)

        expected = (
            '<pv:system installedPower="2310" installationType="FREE_STANDING" dateStartup="2018-12-24" selfShading="true">'
            '<pv:module type="CSI" />'
            '<pv:inverter>'
            '<pv:efficiency xsi:type="pv:EfficiencyConstant" percent="98" />'
            '</pv:inverter>'
            '<pv:losses>'
            '<pv:dcLosses snowPollution="2.5" cables="4" mismatch="1" />'
            '<pv:acLosses transformer="1.5" cables="1" />'
            '</pv:losses>'
            '</pv:system>'
        )
        actual = system.to_xml()
        self.assertEqual(actual, expected)
