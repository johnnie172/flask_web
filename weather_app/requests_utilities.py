

import urllib
import requests
from weather_app import consts
import logging

# todo adding api for all cities in the world
logger = logging.getLogger(__name__)


def check_for_internet_connection(host='http://google.com'):

    try:
        urllib.request.urlopen(host, timeout=2)
        logger.info(consts.INTERNET_CONNECTION_OK_MESSEGE)
        return True
    except:
        logger.exception(consts.INTERNET_CONNECTION_FAIL_MESSEGE)
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

    logger.info('The params are: {}'.format(params))
    api_result = requests.get(consts.WEB_FOR_WEATHER, params)
    logger.info('The api request is: {}'.format(api_result))
    api_response = api_result.json()
    logger.info('The api response is: {}'.format(api_response))

    if 'request' not in api_response:
        logger.error('No response from api')
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


