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
        risk_points_data = fetch_data(GEOJSON_URLS["risk_points"])
        if "error" in risk_points_data:
            return Response({"error": risk_points_data["error"]}, status=500)
        return Response(risk_points_data)  # Return data wrapped in DRF's Response
    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(['GET'])
def main_canal(request):
    try:
        main_canal_data = fetch_data(GEOJSON_URLS["main_canal"])
        if "error" in main_canal_data:
            return Response({"error": main_canal_data["error"]}, status=500)
        return Response(main_canal_data)

    except requests.RequestException as e:
        return {"error": str(e)}



@api_view(['GET'])
def districts_boundary(request):
    try:
        districts_boundary_data = fetch_data(GEOJSON_URLS["districts_boundary"])
        if "error" in districts_boundary_data:
            return Response({"error": districts_boundary_data["error"]}, status=500)
        return Response(districts_boundary_data)
    except requests.RequestException as e:
        return {"error": str(e)}
