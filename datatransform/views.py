import pika
import requests
from background_task.models import CompletedTask
from pipeline.model_to_pipeline import task_executor
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import log_utils
from .models import Task, Pipeline
# Create your views here.

from django.http import JsonResponse, HttpResponse
import pandas as pd
import json
import uuid

GEOJSON_URLS = {
    "risk_points": "http://flood.bangkok.go.th:8443/geoserver/open_lift/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=open_lift%3Arisk_point&maxFeatures=50&outputFormat=application%2Fjson",
    "main_canal": "http://flood.bangkok.go.th:8443/geoserver/open_lift/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=open_lift%3Amain_canal&maxFeatures=50&outputFormat=application%2Fjson",
    "districts_boundary": "http://flood.bangkok.go.th:8443/geoserver/Bangkok_TH/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=Bangkok_TH%3AADMIN_DISTRICT_BND&maxFeatures=50&outputFormat=application%2Fjson"
}


def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}


@api_view(['GET'])
def risk_points(request):
    try:
        print(GEOJSON_URLS["risk_points"])
        risk_points_data = fetch_data(GEOJSON_URLS["risk_points"])
        print(f"fetched data {risk_points_data}")
        dict_data = json.dumps(risk_points_data)
        print(f"dict_data {dict_data}")
        data = json.loads(dict_data)
        print(f"dump file data {data}")
        return data
    except Exception as e:
        return {"error": str(e)}


@api_view(['GET'])
def main_canal(request):
    try:
        main_canal_data = fetch_data(GEOJSON_URLS["main_canal"])
        data = json.loads(main_canal_data)

    except requests.RequestException as e:
        return {"error": str(e)}
    return data


@api_view(['GET'])
def districts_boundary(request):
    try:
        districts_boundary_data = fetch_data(GEOJSON_URLS["districts_boundary"])
        data = json.loads(districts_boundary_data)
        return data
    except requests.RequestException as e:
        return {"error": str(e)}
