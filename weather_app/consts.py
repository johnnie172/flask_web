import os

WEB_FOR_CITY = 'https://ipinfo.io/'
WEB_FOR_WEATHER = 'http://api.weatherstack.com/current'

ACCESS_KEY = os.environ.get['WEATHER_KEY']

INTERNET_CONNECTION_OK_MESSEGE = 'Internet connection ok!'
INTERNET_CONNECTION_FAIL_MESSEGE = 'Connection to internet failed!'