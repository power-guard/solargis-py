# solargis-py


## About

A Python client for querying the SolarGIS API.

## Example usage

```python
import datetime as dt
from solargis import SolarGisClient
from solargis.request import DataDeliveryRequest, Processing, \
    Key, Summarization, Site


api_key = 'demo'
site_id = 'demo_site'
name = 'Demo site'
latitude = 48.61259
longitude = 20.827079

date_from = dt.date(2014, 4, 28)
date_to = dt.date(2014, 4, 28)

proc = Processing(Summarization.HOURLY, Key.GHI.value, terrain_shading=True)
site = Site(site_id, latitude, longitude, name)

request = DataDeliveryRequest(date_from, date_to, site, proc)

client = SolarGisClient(api_key)
response = client.dispatch_request(request)

print(response.data)
```

**Sample output**

```python
{
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
```

## Run unit tests

From the root directory, run the following command:

```bash
python -m unittest -v
```

To get coverage stats:

```bash
coverage run -m unittest
coverage report
```

## References

[Solargis API User Guide](https://wiki.solargis.com/display/public/Solargis+API+User+Guide)
