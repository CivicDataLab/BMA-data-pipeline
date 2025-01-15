import requests
from typing import Dict, Optional, Union
from urllib.parse import urlparse, parse_qs
from django.conf import settings
from dataclasses import dataclass
from decouple import config
from .constants import BUDGET_MIS_API
@dataclass
class APIResponse:
    success: True
    data: Optional[Dict] = None
    error: Optional[Dict] = None
    status_code: int = 200


class BaseAPIClient:
    def __init__(self, base_url: str, timeout: int = 3000, auth: tuple = None):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.auth = auth

    def _make_request(self, endpoint: str, method: str = 'GET', params: Dict = None) -> APIResponse:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = APIResponse()

        try:
            req_response = requests.request(
                method=method,
                url=url,
                params=params,
                timeout=self.timeout,
                auth=self.auth
            )
            response.raise_for_status()
            response.data = req_response.json()
            response.status_code = req_response.status_code
            return APIResponse(success=True, data=response.json(), status_code=response.status_code)
        except requests.exceptions.HTTPError as e:

            response.success = False,
            response.error = f"HTTP Error: {str(e)}",
            response.status_code = e.response.status_code if e.response else 500
            return response

        except requests.exceptions.RequestException as e:

            response.success = False,
            response.error = f"Request Error:{str(e)}",
            response.status_code = 500


class GeoServerClient:
    def __init__(self, timeout=3000):
        self.timeout = timeout

    def _parse_url(self, url: str) -> tuple:
        parsed = urlparse(url)
        base_url = f"{parsed.scheme}://{parsed.netloc}"
        endpoint = parsed.path
        params = parse_qs(parsed.query)
        return base_url, endpoint, params

    def get_geojson(self, url: str) -> APIResponse:
        response = APIResponse(success=True)
        # base_url, endpoint, params = self._parse_url(url)

        try:
            req_response = requests.get(
                url=url,
                timeout=30
            )
            req_response.raise_for_status()
            response.success = True
            response.data = req_response.json()
            response.status_code = req_response.status_code
            return response
        except requests.exceptions.RequestException as e:
            response.success = False
            response.error = f"Request Error: {str(e)}"
            response.status_code = 500
            return response


class BudgetMISClient(BaseAPIClient):
    def __int__(self):
        super().__init__(base_url=BUDGET_MIS_API)
        self.auth = (config("BUDGET_API_USERNAME"), config("BUDGET_API_PASSWORD"))

    def fetch_budget_data(self, endpoint: str, params: Dict = None) -> APIResponse:
        return self._make_request(endpoint=endpoint, method='GET', params=params, auth=self.auth)


