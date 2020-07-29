

import unittest
import utilities
import consts


class TestUtilities(unittest.TestCase):

    def setUp(self):
        self.weather_dict = {
            'city_name': 'Tel Aviv-Yafo', 'local_time': '2020-07-19 13:47',\
                    'current_temp': 30, 'current_desc': 'Sunny', 'current_humidity': 59,\
                    'current_visibility': 7
        }

    def test_visibility_scale_to_desc(self):
        self.assertEqual(utilities.visibility_scale_to_desc(7), 'Good')
        self.assertEqual(utilities.visibility_scale_to_desc(8), 'Very good')

    def test_change_desc_to_alphabet_only(self):
        self.assertEqual(utilities.change_desc_to_alphabet_only(['Sunny']), 'Sunny')
        self.assertEqual(utilities.change_desc_to_alphabet_only(['']), '')
        self.assertEqual(utilities.change_desc_to_alphabet_only(['Mist, Rain With Thunderstorm']),\
                         'Mist, Rain With Thunderstorm')

    def test_make_string_for_weather(self):
        self.assertEqual(utilities.make_string_for_weather(self.weather_dict),\
                         'Now 2020-07-19 13:47 at Tel Aviv-Yafo the weather is Sunny. \ntemp is 30°C, humidity: 59% and the visibility is 7.')
        self.weather_dict['city_name'] = 'delhi'
        self.assertEqual(utilities.make_string_for_weather(self.weather_dict),\
                         'Now 2020-07-19 13:47 at delhi the weather is Sunny. \ntemp is 30°C, humidity: 59% and the visibility is 7.')