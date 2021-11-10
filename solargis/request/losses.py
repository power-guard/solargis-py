import xml.etree.ElementTree as ET

from solargis.abstractelement import AbstractElement

class DcLosses(AbstractElement):
    '''	Estimation of power losses on the DC side. If the element is missing,
    the specific DC losses are estimated by default as:

    snowPolution: 2.5%
    cables: 2.0%
    mismatch: 1.0%
    '''
    def __init__(self, snow_pollution: float , cables: float,
        mismatch: float, monthly_snow_pollution=None):

        self.snow_pollution = snow_pollution
        self.monthly_snow_pollution = monthly_snow_pollution
        self.cables = cables
        self.mismatch = mismatch

        self.prefix = 'pv'
        self.element_name = 'dcLosses'

    def to_element(self) -> ET.Element:
        if self.snow_pollution is None and \
            self.monthly_snow_pollution is None and \
            self.cables is None and \
            self.mismatch is None:
            return None

        attributes = dict()
        if self.monthly_snow_pollution is not None:
            attributes['monthlySnowPollution'] = self.monthly_snow_pollution
        elif self.snow_pollution is not None:
            attributes['snowPollution'] = str(self.snow_pollution)

        if self.cables is not None:
            attributes['cables'] = str(self.cables)
        if self.mismatch is not None:
            attributes['mismatch'] = str(self.mismatch)

        return ET.Element(self.get_element_name(), attrib=attributes)


class AcLosses(AbstractElement):
    """Estimation of power losses on the AC side. If the element is missing,
    the specific AC losses are estimated by default as:

    transformer: 1.0%
    cables: 0.5%
    """
    def __init__(self, transformer: float, cables: float):
        self.transformer = transformer
        self.cables = cables

        self.prefix = 'pv'
        self.element_name = 'acLosses'

    def to_element(self) -> ET.Element:
        if self.transformer is None and self.cables is None:
            return None
        attributes = dict()
        if self.transformer is not None:
            attributes['transformer'] = str(self.transformer)
        if self.cables is not None:
            attributes['cables'] = str(self.cables)
        return ET.Element(self.get_element_name(), attrib=attributes)


class Losses(AbstractElement):
    def __init__(self, ac_losses: AcLosses, dc_losses: DcLosses):
        self.ac_losses = ac_losses
        self.dc_losses = dc_losses

        self.prefix = 'pv'
        self.element_name = 'losses'

    def to_element(self) -> ET.Element:
        ac = self.ac_losses.to_element()
        dc = self.dc_losses.to_element()

        if ac is None and dc is None:
            return None

        losses = ET.Element(self.get_element_name())
        if ac is not None:
            losses.append(ac)
        if dc is not None:
            losses.append(dc)

        return losses
