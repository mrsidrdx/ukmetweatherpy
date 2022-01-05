from django.urls import path
from apis import views

urlpatterns = [
    path('get-weather-data/', views.GetClimateChangeDataView.as_view(), name='get_weather_data'),
]