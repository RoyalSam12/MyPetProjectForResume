from django.urls import path, include

from . import views

app_name = 'mpage'
urlpatterns = [
    path('', views.index, name='index'),
    path('staff/', include('staff.urls')),
    path('weather/', include('weather.urls'))
]
