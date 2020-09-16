from django.shortcuts import render

from .weather_check import check_weather


def weather(requests):
    if requests.GET.get('ask'):
        context = check_weather(requests.GET.get('text'))
        return render(requests, 'weather/index.html', context)
    else:
        context = {}
        return render(requests, 'weather/index.html', context)
