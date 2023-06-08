from django.urls import path

from .views import api_rest_framework

urlpatterns = [
    path('post',api_rest_framework,name='restframework'),
]