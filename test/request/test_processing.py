import unittest

from solargis.exception import ValidationException
from solargis.request import Key, Processing, Summarization, TimestampType


class TestProcessing(unittest.TestCase):

    def test_processing_element_attributes_only(self):
        proc = Processing(Summarization.DAILY, Key.GHI.value)
        expected = '<processing summarization="DAILY" key="GHI" />'
        actual = proc.to_xml()
        self.assertEqual(actual, expected)

    def test_processing_element_with_children(self):
        key = ' '.join((Key.GHI.value, Key.DNI.value))
        tz = 'GMT+09'
        proc = Processing(Summarization.DAILY, key, tz, TimestampType.CENTER)
        expected = (
            '<processing summarization="DAILY" key="GHI DNI">'
            '<timeZone>GMT+09</timeZone>'
            '<timestampType>CENTER</timestampType>'
            '</processing>'
            )
        actual = proc.to_xml()
        self.assertEqual(actual, expected)

    def test_processing_validate_zero_padded_timezone(self):
        args = (Summarization.DAILY, Key.GTI.value, 'GMT+9')
        self.assertRaises(ValidationException, Processing, *args)
