import datetime as dt

from solargis.exception import ValidationException


class Validator():

    @staticmethod
    def not_none(value, param_name):
        if value is None:
            raise ValidationException(f'{param_name} must not be None')

    @staticmethod
    def str_not_none_or_blank(value, param_name):
        if value is None or len(value) == 0:
            raise ValidationException(f'{param_name} must not be blank or empty')

    @staticmethod
    def value_in_enum(value, enum):
        try:
            if value in enum:
                return
        except Exception:
            pass
        raise ValidationException(f'"{value}" does not belong to {enum.__name__}')

    @staticmethod
    def value_in_range(value, lower_bound, upper_bound, param_name):
        if not (lower_bound <= value <= upper_bound):
            raise ValidationException(f'{param_name} ({value}) not in range between {lower_bound} and {upper_bound}')

    @staticmethod
    def greater_than(value, min_value, param_name):
        if not value > min_value:
            raise ValidationException(f'{param_name} must be greater than {min_value} (was {value})')

    @staticmethod
    def horizon_string(value):
        """Validates a string of this form: space-delimited list of float
        number pairs [azimuth in degrees:0-360]:[horizon height in degrees:0-90]
        """
        try:
            for pair in value.split(' '):
                s = pair.split(':')
                if len(s) != 2:
                    raise ValidationException(f'Invalid horizon string. "{pair}" is not a valid azimuth:horizon height pair')

                azimuth, horizon = float(s[0]), float(s[1])

                Validator.value_in_range(azimuth, 0, 360, 'Azimuth')
                Validator.value_in_range(horizon, 0, 90, 'Horizon')

        except ValueError:
            raise ValidationException('Invalid horizon string. All data pairs must be floating poitn numbers.')

    @staticmethod
    def date_range(start_date: dt.datetime, end_date: dt.datetime, max_span: int):
        if not start_date <= end_date:
            raise ValidationException('Start date must precede end date.')
        span = end_date - start_date
        if span.days > max_span:
            raise ValidationException(f'Date range exceeds maximum span ({span.days} > {max_span})')

    @staticmethod
    def gmt_timezone(value):
        msg = 'Timezone must be expressed as "GMT[+-][number of hours zero padded]"'

        if type(value) != str:
            raise ValidationException(msg)

        if len(value) != 6:
            raise ValidationException(msg)

        gmt = value[:3]
        if 'GMT' != gmt:
            raise ValidationException(msg)

        sign = value[3:4]
        if sign != '+' and sign != '-':
            raise ValidationException(msg)

        hours = value[4:6]
        try:
            hours = int(hours)
        except ValueError:
            raise ValidationException(msg)

        if not (0 < hours < 24):
            raise ValidationException(msg)
