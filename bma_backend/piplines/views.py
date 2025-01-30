# pipelines/views.py
from django.http import JsonResponse
from .api_client import GeoServerClient
from .constants import GEOJSON_URLS
from .api_client import BudgetMISClient

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



def get_budget_mis_data(request):
    params = dict(request.GET.items())

    params.setdefault('source_id', '01')
    params.setdefault('book_id', '0')
    params.setdefault('fiscal_year', '66')
    params.setdefault('department_id', '11000000')
    params.setdefault('exp_object_id', '07')
    client = BudgetMISClient()
    response = client.get_budget_data(params)
    return JsonResponse(response, status=response["status_code"])



