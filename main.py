from flask import Flask, request, render_template, redirect
from weather_app import requests_utilities, utilities
import sys
import logging

app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    return render_template('index.html', show_home_icon='no')

@app.route('/weather', methods=['GET'])
def get_weather():
    #todo get exepctions and error
    try:
        client_ip = request.headers.get('X-Forwarded-For', request.headers.get('X-Real-IP'))
        city = request.args.get('query', client_ip)
        api_response = requests_utilities.get_weather_by_location_json(city)
        weather_dict = requests_utilities.get_info_from_json(api_response)
        weather_dict['current_visibility'] = utilities.visibility_scale_to_desc(weather_dict['current_visibility'])
        weather_dict['current_desc'] = utilities.change_desc_to_alphabet_only(weather_dict['current_desc'])
        weather_str = utilities.make_string_for_weather(weather_dict)
    except:
        raise Exception('An error occurred!')
    
    return render_template('weather.html', weather_str=weather_str, api_response=api_response, weather_dict=weather_dict)

@app.route('/choose_city', methods=['GET'])
def choose_city():
    return render_template('choose_city.html')

@app.route('/nasa')
def nasa():
    return render_template('nasa.html')


if __name__ == "__main__":
    app.run(debug=True)
