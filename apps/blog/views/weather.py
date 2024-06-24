import requests
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class WeatherService:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        self.api_key = settings.OPENWEATHERMAP_API_KEY

    def get_weather(self):
        location = f'?lat={self.lat}&lon={self.lon}'
        extra = '&exclude=minutely,hourly,alerts'
        rest = f'&appid={self.api_key}&units=metric'
        base_url = 'https://api.openweathermap.org/data/2.5/weather'

        response = requests.get(f"{base_url}{location}{extra}{rest}")
        data = response.json()
        if response.status_code == 200:
            weather = {
                'temperature': round(data['main']['temp']),
                'description': data['weather'][0]['description'].capitalize()
            }
            return weather
        return None


class WeatherAPIView(APIView):
    def get(self, request, format=None):
        lat = request.query_params.get('lat')
        lon = request.query_params.get('lon')
        if not lat or not lon:
            return Response(
                {"error": "Latitude and longitude are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        weather_service = WeatherService(lat, lon)
        weather = weather_service.get_weather()
        if weather:
            return Response(weather, status=status.HTTP_200_OK)
        return Response(
            {"error": "Unable to fetch weather data"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
