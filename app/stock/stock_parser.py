from typing import List, Optional

import requests

from app.utils import create_url, parse_json_response


class StockParser:
    def __init__(self, domain_url: str, auth_headers: dict) -> None:
        self.domain_url = domain_url
        self.auth_headers = auth_headers

    def _get_stock_response(self, updated_at: str = '') -> requests.Response:
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
        stock_response = self._get_stock_response(updated_at)
        return parse_json_response(stock_response)

    @staticmethod
    def _extract_stock_states(parsed_stock_json: dict) -> Optional[List]:
        embedded = parsed_stock_json.get('_embedded')
        if embedded:
            return embedded.get('stockStates')
        return None

    def get_stock_states(self) -> Optional[List]:
        stock_json = self.get_stock()
        return self._extract_stock_states(stock_json)
