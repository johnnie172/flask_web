

import unittest
import mock
import user_input_utilities
import consts


class TestInputUtilities(unittest.TestCase):

    def setUp(self):
        self.city = 'Tel Aviv'

    def test_choose_diffrent_city_no_differense(self):
        with mock.patch('builtins.input', return_value="no"):
            self.assertEqual(user_input_utilities.choose_diffrent_city(self.city), 'Tel Aviv')

    def test_choose_diffrent_city_with_changes(self):
        with mock.patch('builtins.input', return_value="delhi"):
            self.assertEqual(user_input_utilities.choose_diffrent_city(self.city), 'Delhi')