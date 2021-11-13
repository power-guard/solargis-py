"""
Client for downloading data from the SolarGIS API.
"""
import requests

from solargis.exception import RequestException, ResponseParsingError
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

        try:
            response = requests.post(uri, data=data, headers=headers, timeout=self.TIMEOUT)
            response.raise_for_status()

            return DataDeliveryResponse.from_xml(response.text)

        except ResponseParsingError as e:
            raise
        except requests.exceptions.HTTPError as e:
            raise
        except Exception as e:
            raise RequestException('An unknown error occurred') from e
