# pipelines/views.py
from django.http import JsonResponse
from .api_client import GeoServerClient, BudgetMISClient
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

def get_budget_data(request):
    client = BudgetMISClient()
    response = client.fetch_budget_data(endpoint="budget/report", params={"year": 2567)

    return JsonResponse({
        'success': response.success,
        'data': response.data,
        'error': response.error
    }, status=response.status_code)

