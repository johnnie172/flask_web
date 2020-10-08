

def visibility_scale_to_desc(current_visibility_int):

    current_visibility_dict = {
        0 : 'Dense fog', 1 : 'Thick fog',
        2 : 'Fog', 3 : 'Moderate fog',
        4 : 'Mist or thin fog', 5 : 'Poor',
        6 : 'Moderate', 7 : 'Good',
        8 : 'Very good', 9 : 'Exceptional', 10 : 'Exceptional'
    }

    current_visibility_str = current_visibility_dict.get(current_visibility_int, "unknown")

    return current_visibility_str


def change_desc_to_alphabet_only(desc_string):

    new_desc = ''
    for string in desc_string:
        new_desc += string
    new_desc.strip("'")

    return new_desc


def make_string_for_weather(weather_dict):

    time = weather_dict['local_time']
    city = weather_dict['city_name']
    desc = weather_dict['current_desc']
    temp = weather_dict['current_temp']
    hum = weather_dict['current_humidity']
    vis = weather_dict['current_visibility']

    return "Now {} at {} the weather is {}. \ntemp is {}°C, humidity: {}% and the visibility is {}."\
        .format(time, city, desc, temp, hum, vis)