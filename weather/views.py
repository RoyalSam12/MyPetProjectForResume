from django.shortcuts import render

from .weather_check import check_weather, check_weather_daily


def weather(requests):
    if requests.GET.get('ask'):
        context = check_weather(requests.GET.get('text'))
        return render(requests, 'weather/index.html', context)
    else:
        context = {}
        return render(requests, 'weather/index.html', context)


def weather_week(requests, city, lon, lat):
    context = check_weather_daily(city=city, lon=lon, lat=lat)
    return render(requests, 'weather/week.html', context)
