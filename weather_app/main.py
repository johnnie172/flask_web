

import requests_utilities
import user_input_utilities
import utilities
import consts
import logging

logger = logging.getLogger(__name__)




if __name__ == '__main__':
    #todo change if else
    if requests_utilities.check_for_internet_connection():
        city = requests_utilities.get_user_location()
        city = user_input_utilities.choose_diffrent_city(city)
        api_response = requests_utilities.get_weather_by_location_json(city)
        weather_dict = requests_utilities.get_info_from_json(api_response)
        weather_dict['current_visibility'] = utilities.visibility_scale_to_desc(weather_dict['current_visibility'])
        weather_dict['current_desc'] = utilities.change_desc_to_alphabet_only(weather_dict['current_desc'])
        print(utilities.make_string_for_weather(weather_dict))
    else:
        logger.error(consts.INTERNET_CONNECTION_FAIL_MESSEGE)