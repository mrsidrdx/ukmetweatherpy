"""ukmetweatherpy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import TemplateView

schema_view = get_schema_view(
   openapi.Info(
      title="UK Met Office Weather API",
      default_version='v1',
      description='''
        This is a simple API for the UK Met Office's weather data.

        The following data points are available for reference:

        Region = UK, England, Wales, Scotland, Northern_Ireland, England_and_Wales, England_N, England_S, Scotland_N, Scotland_E, Scotland_W, England_E_and_NE, England_NW_and_N_Wales, Midlands, East_Anglia, England_SW_and_S_Wales, England_SE_and_Central_S
        
        Parameter = Tmax, Tmin, Tmean, Sunshine, Rainfall, Raindays1mm, AirFrost

        Here limit and offset are used for pagination purposes.
        Limit is the number of results to return, and offset is the number of results to skip.
      ''',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apis.urls')),
    path('api-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
