from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient
from ..serializers import ClimateChangeInfo, ClimateChangeInfoSerializer
from ..views import *
import random


# initialize the APIClient app
client = APIClient()

class GetClimateChangeDataTest(TestCase):
    """ Test module for GET Weather API """

    def test_get_valid_single_response(self):
        limit = random.randint(1, 10)
        offset = random.randint(1, 10)
        Region = ['UK', 'England', 'Wales', 'Scotland', 'Northern_Ireland', 'England_and_Wales', 'England_N', 'England_S', 'Scotland_N', 'Scotland_E', 'Scotland_W', 'England_E_and_NE', 'England_NW_and_N_Wales', 'Midlands', 'East_Anglia', 'England_SW_and_S_Wales', 'England_SE_and_Central_S']
        Parameter = ['Tmax', 'Tmin', 'Tmean', 'Sunshine', 'Rainfall', 'Raindays1mm', 'AirFrost']
        region = random.choice(Region)
        parameter = random.choice(Parameter)
        response = client.get('/api/get-weather-data/', data = {'limit' : limit, 'offset' : offset, 'region': region, 'parameter': parameter}, format='json')
        response_new = parse_weather_data(region, parameter)
        data_points = response_new['data_points']
        climate_change_info_list = []
        for data in data_points:
            climate_change_object = ClimateChangeInfo(
                year = data[0],
                jan = data[1],
                feb = data[2],
                mar = data[3],
                apr = data[4],
                may = data[5],
                jun = data[6],
                jul = data[7],
                aug = data[8],
                sep = data[9],
                oct = data[10],
                nov = data[11],
                dec = data[12],
                win = data[13],
                spr = data[14],
                sum = data[15],
                aut = data[16],
                ann = data[17]
            )
            climate_change_info_list.append(climate_change_object)
        # the many param informs the serializer that it will be serializing more than a single climate change object.
        serializer = ClimateChangeInfoSerializer(climate_change_info_list, many=True)
        self.assertEqual(response.data['results'], serializer.data[offset:offset+limit])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_response(self):
        limit = random.randint(1, 10)
        offset = random.randint(1, 10)
        response = client.get('/api/get-weather-data/', data = {'limit' : limit, 'offset' : offset, 'region': 'India', 'parameter': 'Rainfall'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_request_method(self):
        response = client.post('/api/get-weather-data/', data = {'limit' : 10, 'offset' : 10, 'region': 'England', 'parameter': 'Rainfall'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)