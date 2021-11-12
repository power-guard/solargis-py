import unittest
from unittest.mock import Mock
import datetime as dt

import xml.etree.ElementTree as ET

from solargis.request import DataDeliveryRequest

class TestDataDeliveryRequest(unittest.TestCase):
    def test_happy_path(self):
        start_date = dt.date(2021, 1, 1)
        end_date = dt.date(2021, 1, 2)

        site = Mock()
        site.to_element = Mock(return_value=ET.Element('site'))

        proc = Mock()
        proc.to_element = Mock(return_value=ET.Element('processing'))

        request = DataDeliveryRequest(start_date, end_date, site, proc)
        xml = request.to_xml()

        expected = (
            '<ws:dataDeliveryRequest dateFrom="2021-01-01" dateTo="2021-01-02" '
            'xmlns="http://geomodel.eu/schema/data/request" '
            'xmlns:ws="http://geomodel.eu/schema/ws/data" '
            'xmlns:geo="http://geomodel.eu/schema/common/geo" '
            'xmlns:pv="http://geomodel.eu/schema/common/pv" '
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            '<site />'
            '<processing />'
            '</ws:dataDeliveryRequest>'
        )

        self.assertEqual(xml, expected)

