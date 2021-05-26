from typing import Dict, List, Optional

import requests


def create_url(urls: List[str], params: Optional[Dict] = None) -> str:
    urls_str = ''.join(urls)
    if params:
        if not isinstance(params, dict):
            raise TypeError(
                f'params should be <class \'dict\'>, not {type(params)}'
                )
        params_str = '&'.join([f'{key}={val}' for key, val in params.items()])
        return '?'.join((urls_str, params_str))
    return urls_str


def parse_json_response(response: requests.Response) -> dict:
    return response.json()
