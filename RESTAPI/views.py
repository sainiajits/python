from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics
# Create your views here.

global data
data = ["Test"]

class presonView(APIView):
    def get(self, request, format=None):
        message = {
            'Response':200,
            'Message':"Welcome to Django Rest API",
            'data':data
        }
        return Response(message)

    def post(self, request, format=None):
        datam = request.data
        name = datam.get('Name', None)
        data.append(name)
        message = {
            'Response':200,
            'Message':"Welcome to Django Rest API",
            'data':data
        }
        return Response(message)

from .serializer import DummySerializer

class WeatherView(generics.CreateAPIView):
    serializer_class = DummySerializer
    def create(self, request, *args, **kwargs):
        try:
            zip = request.data.post('zip')
            city = request.data.post('city')
            age = request.data.post('age')
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({
                "Message": "Failed"
            })

