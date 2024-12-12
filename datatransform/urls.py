from django.urls import path

from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/v1/risk-points', views.risk_points, name='risk_points'),
    path('api/v1/main-canal', views.main_canal, name='main_canal'),
    path('api/v1/districts-boundary', views.districts_boundary, name='districts_boundary'),
]
