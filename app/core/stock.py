import requests
from app.utils import create_url, parse_json_response


class StockParser:
    def __init__(self, domain_url: str, auth_headers: dict) -> None:
        self.domain_url = domain_url
        self.auth_headers = auth_headers

    def _get_stock(self, updated_at: str = '') -> requests.Response:
        url_parts = [
            self.domain_url,
            '/api/v1/stock/goods',
            ]
        params = {'limit': '1000000'}
        if updated_at:
            params['updatedAt'] = updated_at
        request_url = create_url(url_parts, params)
        response = requests.get(
            request_url,
            headers=self.auth_headers,
            )
        response.raise_for_status()
        return response

    def get_stock(self, updated_at: str = '') -> dict:
        stock_response = self._get_stock(updated_at)
        return parse_json_response(stock_response)
