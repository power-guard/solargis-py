"""
Client for downloading data from the SolarGIS API.
"""
import requests

from solargis.request import DataDeliveryRequest
from solargis.response import DataDeliveryResponse


class SolarGisClient():

    TIMEOUT = (3, 3.04)

    def __init__(self, api_key: str):
        self.api_key = api_key

    def dispatch_request(self, request: DataDeliveryRequest):
        uri = f'https://solargis.info/ws/rest/datadelivery/request?key={self.api_key}'
        headers = {'Content-Type': 'application/xml'}
        data = request.to_xml().encode('utf8')

        with requests.post(uri, data=data, headers=headers, timeout=self.TIMEOUT) as response:
            return DataDeliveryResponse.from_xml(response.text)
