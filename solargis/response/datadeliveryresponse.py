import xml.etree.ElementTree as ET

from solargis.exception import ResponseParsingError, ValidationException


class DataDeliveryResponse():

    XML_NAMESPACES = {
        'data':'http://geomodel.eu/schema/ws/data'
    }

    def __init__(self):
        self.raw = None
        self.columns = []
        self.data = dict()

    @staticmethod
    def from_xml(xml):
        try:
            root = ET.fromstring(xml)
            root = root.find('data:site', DataDeliveryResponse.XML_NAMESPACES)

            if root is None:
                raise ValidationException('failed to find root element')

            res = DataDeliveryResponse()
            res.raw = xml

            # find column names
            columns_tag = root.find('data:columns', DataDeliveryResponse.XML_NAMESPACES)
            columns = columns_tag.text.split(' ')
            res.columns = columns

            # build data dictionary
            data = dict()
            for column in columns:
                data[column] = dict()

            row_tags = root.findall('data:row', DataDeliveryResponse.XML_NAMESPACES)
            for row in row_tags:
                timestamp = row.attrib.get('dateTime')
                values = row.attrib.get('values')
                values = values.split(' ')

                for i, value in enumerate(values):
                    col_name = columns[i]
                    data[col_name][timestamp] = float(value)

            res.data = data

            return res
        except Exception as e:
            raise ResponseParsingError('Failed to parse XML response') from e
