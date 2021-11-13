import datetime as dt
import xml.etree.ElementTree as ET
from enum import Enum

from solargis.abstractelement import AbstractElement
from solargis.validator import Validator


class InstallationType(Enum):
    """This property of the PV system helps to estimate how
    modules are cooled by air. For sloped roof with PV modules
    on rails tilted at the same angle as the roof choose
    'ROOF_MOUNTED' value. For PV modules incorporated into
    building facade choose 'BUILDING_INTEGRATED' value.
    This option is considered as the worst ventilated.
    As the best ventilated option is considered 'FREE_STANDING'
    installation. This typically means stand-alone installation
    on tilted racks anchored into the ground. Also choose this
    option if a PV system is installed on a flat roof."""

    FREE_STANDING = 'FREE_STANDING'
    ROOF_MOUNTED = 'ROOF_MOUNTED'
    BUILDING_INTEGRATED = 'BUILDING_INTEGRATED'


class System(AbstractElement):
    """Parametrization of the PV system. Required for simulating PVOUT parameter."""

    DATE_FORMAT = '%Y-%m-%d'

    def __init__(self,
                 installed_power: float,
                 module,
                 inverter,
                 losses,
                 topology=None,
                 installation_type: InstallationType = None,
                 date_startup: dt.date = None,
                 self_shading: bool = None):

        Validator.not_none(module, 'module')
        Validator.not_none(inverter, 'inverter')
        Validator.not_none(losses, 'losses')
        Validator.greater_than(installed_power, 0, 'installed power')

        if installation_type is not None:
            Validator.value_in_enum(installation_type, InstallationType)

        self.installed_power = installed_power
        self.module = module
        self.inverter = inverter
        self.losses = losses
        self.topology = topology
        self.installation_type = installation_type
        self.date_startup = date_startup
        self.self_shading = self_shading

        self.element_name = 'system'
        self.prefix = 'pv'

    def to_element(self):
        attributes = dict()
        attributes['installedPower'] = str(self.installed_power)

        if self.installation_type is not None:
            attributes['installationType'] = self.installation_type.value
        if self.date_startup is not None:
            attributes['dateStartup'] = self.date_startup.strftime(self.DATE_FORMAT)
        if self.self_shading is not None:
            attributes['selfShading'] = str(self.self_shading).lower()

        system = ET.Element(self.get_element_name(), attrib=attributes)
        system.append(self.module.to_element())
        system.append(self.inverter.to_element())
        system.append(self.losses.to_element())

        if self.topology is not None:
            system.append(self.topology.to_element())

        return system
