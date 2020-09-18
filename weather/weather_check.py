from datetime import datetime, timedelta

import requests


def check_weather(city):
    api_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': 'fe6c9ac08e96ecdd33f559f07bc59da7',
        'units': 'metric',
        'lang': 'ru'
    }
    re = requests.get(api_url, params=params)
    if re.status_code == 404:
        data_for_views = {'get_info': False, 'error': 'Данные введены некорректно'}
        return data_for_views
    else:
        data = re.json()
        data_for_views = {
            'lon': data['coord']['lon'],
            'lat': data['coord']['lat'],
            'get_info': True,
            'city_name': data['name'],
            'weather_description': data['weather'][0].get('description'),
            'weather_temp': data['main'].get('temp'),
            'weather_feels_temp': data['main'].get('feels_like'),
            'weather_max_temp': data['main'].get('temp_max')
        }
        return data_for_views


def check_weather_daily(city, lon, lat):
    date = {0: 'Пн', 1: 'Вт', 2: 'Cр', 3: 'Чт', 4: 'Пт', 5: 'Сб', 6: 'Вс'}
    date_month = {
        1: 'Января', 2: 'Февраля', 3: 'Марта',
        4: 'Апреля', 5: 'Мая', 6: 'Июня',
        7: 'Июля', 8: 'Августа', 9: 'Сентября',
        10: 'Октября', 11: 'Ноября', 12: 'Декабря'
    }
    api_url = 'https://api.openweathermap.org/data/2.5/onecall'
    params = {
        'lon': lon,
        'lat': lat,
        'appid': 'fe6c9ac08e96ecdd33f559f07bc59da7',
        'units': 'metric',
        'lang': 'ru'
    }
    re = requests.get(api_url, params=params)
    data = re.json()
    data_for_views = dict()
    date_now = datetime.now()
    for day_info in data['daily']:
        data_for_views[str(date_now)] = {
            'day_of_week': '{} {} {} года {}'.format(
                str(date_now.date().day),
                date_month.get(date_now.month),
                date_now.year,
                date.get(date_now.weekday())
            ),
            'city': city,
            'temp_day': day_info['temp'].get('day'),
            'temp_min': day_info['temp'].get('min'),
            'temp_max': day_info['temp'].get('max'),
            'temp_night': day_info['temp'].get('night'),
            'temp_eve': day_info['temp'].get('eve'),
            'temp_mor': day_info['temp'].get('morn'),
            'fells_temp_day': day_info['feels_like'].get('day'),
            'fells_temp_night': day_info['feels_like'].get('night'),
            'fells_temp_eve': day_info['feels_like'].get('eve'),
            'fells_temp_mor': day_info['feels_like'].get('morn'),
            'weather_description': day_info['weather'][0].get('description').capitalize()
        }
        date_now += timedelta(days=1)
    return data_for_views

print(check_weather_daily('Киев', 30.52, 50.43))