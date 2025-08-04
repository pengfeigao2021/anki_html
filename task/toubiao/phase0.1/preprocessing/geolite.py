import os
import geoip2.database

CITY_DATABASE = '/Users/AlexG/Downloads/GeoLite2-City.mmdb'
with geoip2.database.Reader(CITY_DATABASE) as reader:
    # response = reader.city('128.101.101.101');
    response = reader.city('222.188.57.78')
    print(response.country.iso_code)
    print(response)