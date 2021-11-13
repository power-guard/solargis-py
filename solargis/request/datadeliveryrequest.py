'''
<ws:dataDeliveryRequest dateFrom="2021-10-06" dateTo="2021-10-31"
    xmlns="http://geomodel.eu/schema/data/request"
    xmlns:ws="http://geomodel.eu/schema/ws/data"
    xmlns:geo="http://geomodel.eu/schema/common/geo"
    xmlns:pv="http://geomodel.eu/schema/common/pv"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

    <site id="PV001" name="ZN100001-35B" lat="33.173251" lng="130.018391">
        <geo:terrain elevation="48" azimuth="270" tilt="10"/>
        <pv:geometry xsi:type="pv:GeometryFixedOneAngle" azimuth="205" tilt="18"/>
        <pv:system installedPower="2310" installationType="FREE_STANDING" selfShading="true" dateStartup="2018-12-24">
            <pv:module type="CSI">
                <pv:degradation>0</pv:degradation>
                <pv:degradationFirstYear>0.8</pv:degradationFirstYear>
                <pv:surfaceReflectance>0.16</pv:surfaceReflectance>
            </pv:module>
            <pv:inverter>
                <pv:efficiency xsi:type="pv:EfficiencyConstant" percent="98"/>
                <!--<pv:efficiency xsi:type="pv:EfficiencyCurve" dataPairs="0:20 50:60 100:80 150:90 233:97.5 350:97 466:96.5 583:96 700:95.5 750:93.33 800:87.5 850:82.35 900:77.8 950:73.7"/>-->
                <pv:limitationACPower>1715</pv:limitationACPower>
            </pv:inverter>
            <pv:losses>
                <!--for dcLosses enter either monthlySnowPollution 12 monthly % numbers or snowPollution as one % number-->
                <pv:dcLosses cables="4" mismatch="1" snowPollution="2.5"/>
                <pv:acLosses cables="1" transformer="1.5"/>
            </pv:losses>
            <pv:topology xsi:type="pv:TopologyRow" relativeSpacing="1.46" type="UNPROPORTIONAL1"/>
        </pv:system>
    </site>

    <processing key="GHI GTI DIF TEMP PVOUT WS WD " summarization="HOURLY" terrainShading="true">
        <timeZone>GMT+09</timeZone>
        <timestampType>CENTER</timestampType>
    </processing>

</ws:dataDeliveryRequest>
'''
import datetime as dt
import xml.etree.ElementTree as ET

from solargis.abstractelement import AbstractElement
from solargis.validator import Validator


class DataDeliveryRequest(AbstractElement):
    DATE_FORMAT = '%Y-%m-%d'

    def __init__(self, date_from: dt.date, date_to: dt.date,
        site, processing):

        Validator.date_range(date_from, date_to, 31)
        Validator.not_none(site, 'site')
        Validator.not_none(processing, 'processing')

        self.date_from = date_from
        self.date_to = date_to

        self.site = site
        self.processing = processing

        self.prefix = 'ws'
        self.element_name = 'dataDeliveryRequest'

    def to_element(self):
        attributes = dict()
        attributes['dateFrom'] = self.date_from.strftime(self.DATE_FORMAT)
        attributes['dateTo'] = self.date_to.strftime(self.DATE_FORMAT)
        attributes['xmlns'] = 'http://geomodel.eu/schema/data/request'
        attributes['xmlns:ws'] = 'http://geomodel.eu/schema/ws/data'
        attributes['xmlns:geo'] = 'http://geomodel.eu/schema/common/geo'
        attributes['xmlns:pv'] = 'http://geomodel.eu/schema/common/pv'
        attributes['xmlns:xsi'] = 'http://www.w3.org/2001/XMLSchema-instance'

        site = self.site.to_element()
        proc = self.processing.to_element()

        element = ET.Element(self.get_element_name(), attrib=attributes)
        element.append(site)
        element.append(proc)

        return element
