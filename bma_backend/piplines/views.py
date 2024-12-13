# pipelines/views.py
from django.http import JsonResponse
from .api_client import GeoServerClient
from .constants import GEOJSON_URLS


def get_geojson_data(request, layer_type):
    if layer_type not in GEOJSON_URLS:
        return JsonResponse({'success': False, 'error': 'Invalid layer type'}, status=400)

    client = GeoServerClient()
    response = client.get_geojson(GEOJSON_URLS[layer_type])

    return JsonResponse({
        'success': response.success,
        'data': response.data,
        'error': response.error
    }, status=response.status_code)
