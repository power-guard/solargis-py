import unittest

from solargis.response import DataDeliveryResponse


class TestDataDeliveryResponse(unittest.TestCase):
    def test_parse_demo_response(self):
        raw = (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><dataDeliveryResponse xmlns="http://geomodel.eu/schema/ws/data" xmlns:ns2="http://geomodel.eu/schema/common/geo"><site id="demo_site" lat="48.61259" lng="20.827079"><metadata>#HOURLY VALUES OF SOLAR RADIATION&#xD;'
            '#&#xD;'
            '#File type: Solargis_TS60&#xD;'
            '#Issued: 2021-11-10 05:15&#xD;'
            '</metadata><columns>GHI</columns><row dateTime="2014-04-28T00:30:00.000Z" values="0.0"/><row dateTime="2014-04-28T01:30:00.000Z" values="0.0"/><row dateTime="2014-04-28T02:30:00.000Z" values="0.0"/><row dateTime="2014-04-28T03:30:00.000Z" values="8.0"/><row dateTime="2014-04-28T04:30:00.000Z" values="109.0"/><row dateTime="2014-04-28T05:30:00.000Z" values="278.0"/><row dateTime="2014-04-28T06:30:00.000Z" values="462.0"/><row dateTime="2014-04-28T07:30:00.000Z" values="618.0"/><row dateTime="2014-04-28T08:30:00.000Z" values="711.0"/><row dateTime="2014-04-28T09:30:00.000Z" values="743.0"/><row dateTime="2014-04-28T10:30:00.000Z" values="477.0"/><row dateTime="2014-04-28T11:30:00.000Z" values="424.0"/><row dateTime="2014-04-28T12:30:00.000Z" values="685.0"/><row dateTime="2014-04-28T13:30:00.000Z" values="381.0"/><row dateTime="2014-04-28T14:30:00.000Z" values="459.0"/><row dateTime="2014-04-28T15:30:00.000Z" values="305.0"/><row dateTime="2014-04-28T16:30:00.000Z" values="130.0"/><row dateTime="2014-04-28T17:30:00.000Z" values="6.0"/><row dateTime="2014-04-28T18:30:00.000Z" values="0.0"/><row dateTime="2014-04-28T19:30:00.000Z" values="0.0"/><row dateTime="2014-04-28T20:30:00.000Z" values="0.0"/><row dateTime="2014-04-28T21:30:00.000Z" values="0.0"/><row dateTime="2014-04-28T22:30:00.000Z" values="0.0"/><row dateTime="2014-04-28T23:30:00.000Z" values="0.0"/></site></dataDeliveryResponse>'
        )

        response = DataDeliveryResponse.from_xml(raw)

        self.assertEqual(raw, response.raw)
        self.assertListEqual(['GHI'], response.columns)

        expected = {
            'GHI': {
                '2014-04-28T00:30:00.000Z': 0.0,
                '2014-04-28T01:30:00.000Z': 0.0,
                '2014-04-28T02:30:00.000Z': 0.0,
                '2014-04-28T03:30:00.000Z': 8.0,
                '2014-04-28T04:30:00.000Z': 109.0,
                '2014-04-28T05:30:00.000Z': 278.0,
                '2014-04-28T06:30:00.000Z': 462.0,
                '2014-04-28T07:30:00.000Z': 618.0,
                '2014-04-28T08:30:00.000Z': 711.0,
                '2014-04-28T09:30:00.000Z': 743.0,
                '2014-04-28T10:30:00.000Z': 477.0,
                '2014-04-28T11:30:00.000Z': 424.0,
                '2014-04-28T12:30:00.000Z': 685.0,
                '2014-04-28T13:30:00.000Z': 381.0,
                '2014-04-28T14:30:00.000Z': 459.0,
                '2014-04-28T15:30:00.000Z': 305.0,
                '2014-04-28T16:30:00.000Z': 130.0,
                '2014-04-28T17:30:00.000Z': 6.0,
                '2014-04-28T18:30:00.000Z': 0.0,
                '2014-04-28T19:30:00.000Z': 0.0,
                '2014-04-28T20:30:00.000Z': 0.0,
                '2014-04-28T21:30:00.000Z': 0.0,
                '2014-04-28T22:30:00.000Z': 0.0,
                '2014-04-28T23:30:00.000Z': 0.0
            }
        }
        self.assertDictEqual(expected, response.data)
