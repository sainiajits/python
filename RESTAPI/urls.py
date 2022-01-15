from django.urls import path, include
from django.conf.urls import defaults
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
    path('', views.presonView.as_view()),
    path('add/', views.WeatherView.as_view()),
]