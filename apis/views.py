import requests

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import ClimateChangeInfo, ClimateChangeInfoSerializer

# Create your views here.

# To ensure data-type consistency, type check is added, 
# if failed then by default 0 will be assigned
def custom_float(num):
    try:
        if type(eval(num)) == float:
            return float(num)
        elif type(eval(num)) == int:
            return int(num)
    except Exception as e:
        return 0

# Parsing climate change data
def parse_weather_data(region, parameter):
    try:
        url = 'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/{0}/date/{1}.txt'.format(parameter, region)
        response = requests.get(url)
        data = response.text.split('\n')
        last_updated_date = ' '.join(data[4].split()[-2:])
        data_points = []
        for row in data[6:-1]:
            data_points.append(list(map(custom_float, row.split())))
        body = {
            'last_updated_date': last_updated_date,
            'data_points': data_points
        }
        return body
    except Exception as e:
        return {'error': 'Invalid region, parameter combination'}

test_param = [
    openapi.Parameter('region', openapi.IN_QUERY, description="Enter region name", type=openapi.TYPE_STRING),
    openapi.Parameter('parameter', openapi.IN_QUERY, description="Enter parameter name", type=openapi.TYPE_STRING),
    openapi.Parameter('limit', openapi.IN_QUERY, description="Enter limit value", type=openapi.TYPE_INTEGER),
    openapi.Parameter('offset', openapi.IN_QUERY, description="Enter offset value", type=openapi.TYPE_INTEGER),
]

class GetClimateChangeDataView(APIView):
    @swagger_auto_schema(
        responses={
            405: openapi.Response('Method Not Allowed', openapi.Schema(type=openapi.TYPE_OBJECT)),
        }
    )
    def post(self, request):
        return Response({'error' : 'Invalid Request Method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    @swagger_auto_schema(
        manual_parameters=test_param,
        responses={
            200: ClimateChangeInfoSerializer(many=True),
            400: openapi.Response('Bad Request', openapi.Schema(type=openapi.TYPE_OBJECT)),
        }
    )
    def get(self, request):
        paginator = LimitOffsetPagination()
        response = parse_weather_data(request.GET['region'], request.GET['parameter'])
        if 'error' in response:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        data_points = response['data_points']
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
        query_set = climate_change_info_list
        context = paginator.paginate_queryset(query_set, request)
        serializer = ClimateChangeInfoSerializer(context, many=True)
        return paginator.get_paginated_response(serializer.data)

if __name__ == '__main__':
    parse_weather_data('England_SE_and_Central_S', 'Rainfall')