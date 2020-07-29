

import urllib
import requests
from weather_app import consts

# todo adding api for all cities in the world

def check_for_internet_connection(host='http://google.com'):

    try:
        urllib.request.urlopen(host, timeout=2)
        return True
    except:
        return False


def get_user_location():

    response = requests.get(consts.WEB_FOR_CITY)
    data = response.json()
    city = data['city']

    return city


def get_weather_by_location_json(city):

    params = {
        'access_key': consts.ACCESS_KEY,
        'query': city
    }
    api_result = requests.get(consts.WEB_FOR_WEATHER, params)
    api_response = api_result.json()

    if 'request' not in api_response:
        raise Exception('Sorry, we could not get the information, please try again.')

    return api_response


def get_info_from_json(api_response):

    weather_dict = {}
    location = api_response['location']
    weather_dict['city_name'] = location['name']
    weather_dict['local_time'] = location['localtime']

    current = api_response['current']
    weather_dict['current_temp'] = current['temperature']
    weather_dict['current_desc'] = current['weather_descriptions']
    weather_dict['current_humidity'] = current['humidity']
    weather_dict['current_visibility'] = current['visibility']

    return weather_dict


