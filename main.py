from flask import Flask, request, render_template, jsonify, redirect
from weather_app import requests_utilities, utilities

app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    #todo get exepctions and error
    city = request.args.get('query', 'fetch:ip')
    api_response = requests_utilities.get_weather_by_location_json(city)
    weather_dict = requests_utilities.get_info_from_json(api_response)
    weather_dict['current_visibility'] = utilities.visibility_scale_to_desc(weather_dict['current_visibility'])
    weather_dict['current_desc'] = utilities.change_desc_to_alphabet_only(weather_dict['current_desc'])
    weather_str = utilities.make_string_for_weather(weather_dict)

    return render_template('weather.html', weather_str=weather_str, api_response=api_response, weather_dict=weather_dict)

@app.route('/choose_city', methods=['GET'])
def choose_city():
    return render_template('choose_city.html')



if __name__ == "__main__":
    app.run(debug=True)
