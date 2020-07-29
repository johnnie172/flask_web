
import unittest
import requests_utilities
import consts


class TestRequestsUtilities(unittest.TestCase):

    def setUp(self):

        self.weather_dict = {
            'city_name': 'Tel Aviv-Yafo', 'local_time': '2020-07-19 13:47',\
            'current_temp': 30, 'current_desc': 'Sunny', 'current_humidity': 59,\
            'current_visibility': 7
        }
        self.weather_json_tlv = {
            'request': {'type': 'City', 'query': 'Tel Aviv-Yafo, Israel', 'language': 'en', 'unit': 'm'}\
            , 'location': \
                {'name': 'Tel Aviv-Yafo', 'country': 'Israel', 'region': 'Tel Aviv',\
                 'lat': '32.068', 'lon': '34.765', 'timezone_id': 'Asia/Jerusalem',\
                 'localtime': '2020-07-19 18:50', 'localtime_epoch': 1595184600, 'utc_offset': '3.0'},\
            'current': {'observation_time': '03:50 PM', 'temperature': 30, 'weather_code': 113,\
                        'weather_icons': ['https://assets.weatherstack.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png'],\
                        'weather_descriptions': ['Sunny'], 'wind_speed': 22, 'wind_degree': 330, 'wind_dir': 'NNW',\
                        'pressure': 1006, 'precip': 0, 'humidity': 52, 'cloudcover': 0, 'feelslike': 34,\
                        'uv_index': 7, 'visibility': 10, 'is_day': 'yes'}}
        self.weather_json_delhi = {
            'request': {'type': 'City', 'query': 'Delhi, India', 'language': 'en', 'unit': 'm'},
             'location': {'name': 'Delhi', 'country': 'India', 'region': 'Delhi', 'lat': '28.667', 'lon': '77.217',
                          'timezone_id': 'Asia/Kolkata', 'localtime': '2020-07-19 21:16', 'localtime_epoch': 1595193360,
                          'utc_offset': '5.50'},
             'current': {'observation_time': '03:46 PM', 'temperature': 32, 'weather_code': 143, 'weather_icons': [
                 'https://assets.weatherstack.com/images/wsymbols01_png_64/wsymbol_0006_mist.png'],
                         'weather_descriptions': ['Mist'], 'wind_speed': 0, 'wind_degree': 0, 'wind_dir': 'N',
                         'pressure': 998, 'precip': 0.2, 'humidity': 80, 'cloudcover': 50, 'feelslike': 35,
                         'uv_index': 1, 'visibility': 4, 'is_day': 'no'}
        }


        self.city_tlv = 'Tel Aviv'

        self.city_delhi = 'Delhi'

    def test_check_for_internet_connection(self):
        self.assertEqual(requests_utilities.check_for_internet_connection(), True)
        self.assertEqual(requests_utilities.check_for_internet_connection('http://gggvvddbfbt.co'), False)

    def test_get_user_location(self):
        #todo test with fake ip
        pass

    def test_get_weather_by_location_json(self):
        tlv_json = requests_utilities.get_weather_by_location_json(self.city_tlv)
        delhi_json = requests_utilities.get_weather_by_location_json(self.city_delhi)
        self.assertEqual(tlv_json['location']['name'], self.weather_json_tlv['location']['name'])
        self.assertEqual(delhi_json['location']['name'], self.weather_json_delhi['location']['name'])


    def test_get_info_from_json(self):
        self.assertEqual(requests_utilities.get_info_from_json(self.weather_json_delhi)['city_name'], 'Delhi')
        self.assertEqual(requests_utilities.get_info_from_json(self.weather_json_tlv)['city_name'],\
                         self.weather_dict['city_name'])
        self.assertEqual(len(requests_utilities.get_info_from_json(self.weather_json_delhi)), 6)
        self.assertEqual(len(requests_utilities.get_info_from_json(self.weather_json_tlv)), 6)