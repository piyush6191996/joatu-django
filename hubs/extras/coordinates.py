import requests
import urllib.parse
from decimal import Decimal
from django.conf import settings




def coordinates_calculation(number, street, postal_code, city, country):
    API_key = settings.GOOGLE_API_KEY
    main_api = "https://maps.googleapis.com/maps/api/geocode/json?"
    address = number+ ' ' + street + ' ' + postal_code + ' ' + city + ' ' + country
    url = main_api + urllib.parse.urlencode({'address':address})+ '&key='+API_key
    json_data = requests.get(url).json()
    lat= Decimal(json_data['results'][0]['geometry']['location']['lat'])
    lng= Decimal(json_data['results'][0]['geometry']['location']['lng'])
    return lat, lng