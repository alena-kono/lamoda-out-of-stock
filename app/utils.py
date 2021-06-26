from json.decoder import JSONDecodeError
from typing import Dict, List, Optional

import requests

from app.exceptions import InvalidJsonError


def create_url(urls: List[str], params: Optional[Dict] = None) -> str:
    if not urls:
        raise ValueError('urls should not be empty list')
    urls_str = ''.join([str(_) for _ in urls])
    if params:
        if not isinstance(params, dict):
            raise TypeError(
                f'params should be <class \'dict\'>, not {type(params)}'
                )
        params_str = '&'.join([f'{key}={val}' for key, val in params.items()])
        return '?'.join((urls_str, params_str))
    return urls_str


def parse_json_response(response: requests.Response) -> dict:
    if not isinstance(response, requests.Response):
        raise TypeError(
            'response should be <class \'requests.Response\',',
            f'not {type(response)}'
            )
    try:
        parsed_json = response.json()
    except JSONDecodeError:
        raise InvalidJsonError()
    return parsed_json
