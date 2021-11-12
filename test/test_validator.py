import unittest
from enum import Enum
import datetime as dt

from solargis.exception import ValidationException
from solargis.validator import Validator

class SampleEnum(Enum):
    A = 0
    B = 1

class TestValidator(unittest.TestCase):
    def test_not_none_pass(self):
        Validator.not_none(1, 'param name')

    def test_not_none_fail(self):
        with self.assertRaises(ValidationException):
            Validator.not_none(None, 'param name')

    def test_str_not_none_or_blank_pass(self):
        Validator.str_not_none_or_blank('foo', 'param name')

    def test_str_not_none_or_blank_fail(self):
        with self.assertRaises(ValidationException):
            Validator.str_not_none_or_blank('', 'param name')
        with self.assertRaises(ValidationException):
            Validator.str_not_none_or_blank(None, 'param name')

    def test_value_in_enum_pass(self):
        Validator.value_in_enum(SampleEnum.A, SampleEnum)

    def test_value_in_enum_fail(self):
        with self.assertRaises(ValidationException):
            Validator.value_in_enum(0, SampleEnum)

    def test_value_in_range_pass(self):
        Validator.value_in_range(5, 0, 10, 'param name')

    def test_value_in_range_fail(self):
        with self.assertRaises(ValidationException):
            Validator.value_in_range(11, 0, 10, 'param name')

    def test_greater_than_pass(self):
        Validator.greater_than(10, 9, 'param name')

    def test_greater_than_fail(self):
        with self.assertRaises(ValidationException):
            Validator.greater_than(9, 10, 'param name')

    def test_horizon_string_pass(self):
        Validator.horizon_string('283.5:2.6 284:2.6 284.5:2.6 285:2.8 285.5:2.8 286:2.8 286.5:2.8')

    def test_horizon_string_fail(self):
        with self.assertRaises(ValidationException):
            Validator.horizon_string('400:20')

        with self.assertRaises(ValidationException):
            Validator.horizon_string('300')

        with self.assertRaises(ValidationException):
            Validator.horizon_string('283.5:2.6 284:2.6 284.5:2.6 285:2.8 285.5:2.8 286:2.8 286.5:2.8a')

    def test_date_range_pass(self):
        start_date = dt.date(2021, 1, 1)
        end_date = dt.date(2021, 1, 10)
        Validator.date_range(start_date, end_date, 20)

    def test_date_range_fail(self):
        start_date = dt.date(2021, 1, 1)
        end_date = dt.date(2021, 1, 10)

        with self.assertRaises(ValidationException):
            Validator.date_range(start_date, end_date, 3)
        with self.assertRaises(ValidationException):
            Validator.date_range(end_date, start_date, 100)

    def test_gmt_timezone_pass(self):
        Validator.gmt_timezone('GMT+02')

    def test_gmt_timezone_fail(self):
        with self.assertRaises(ValidationException):
            Validator.gmt_timezone('GMT+2')
        with self.assertRaises(ValidationException):
            Validator.gmt_timezone(2)
        with self.assertRaises(ValidationException):
            Validator.gmt_timezone('UTC+09')
        with self.assertRaises(ValidationException):
            Validator.gmt_timezone('JST')
        with self.assertRaises(ValidationException):
            Validator.gmt_timezone('GMT+90')