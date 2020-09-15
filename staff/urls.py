from django.urls import path

from . import views

app_name = 'staff'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/dismiss', views.dismiss, name='dismiss'),
    path('<int:pk>/add_detail', views.add_info, name='add')
]
