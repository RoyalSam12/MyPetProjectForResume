from django.urls import path

from . import views

urlpatterns = [
    path('', views.weather, name='weather'),
    path('<city>/<lon>/<lat>/week', views.weather_week, name='week'),

]
