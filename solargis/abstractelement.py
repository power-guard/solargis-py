import xml.etree.ElementTree as ET


class AbstractElement():
    def get_element_name(self) -> str:
        if self.prefix:
            return self.prefix + ':' + self.element_name
        return self.element_name

    def to_element(self) -> ET.Element:
        raise Exception('subclasses must implement this method')

    def to_xml(self) -> str:
        tree = self.to_element()
        return ET.tostring(tree, encoding='unicode')
