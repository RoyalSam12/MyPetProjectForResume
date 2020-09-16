import requests

def check_weather(city):
    api_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': 'fe6c9ac08e96ecdd33f559f07bc59da7',
        'units': 'metric'
    }
    res = requests.get(api_url, params=params)
    data = res.json()
    data_for_views = dict()
    data_for_views['weather_description'] = data['weather'][0].get('main')
    data_for_views['weather_temp'] = data['main'].get('temp')
    data_for_views['weather_feels_temp'] = data['main'].get('feels_like')
    data_for_views['weather_max_temp'] = data['main'].get('temp_max')
    return data_for_views



