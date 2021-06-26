import json

import pytest
from app.exceptions import InvalidJsonError
from app.utils import create_url, parse_json_response


def test_create_url(expected_urls):
    equal_urls = []
    for expected_url in expected_urls:
        created_url = create_url(
            urls=expected_urls[expected_url].get('urls'),
            params=expected_urls[expected_url].get('params'),
            )
        equal_urls.append(created_url == expected_url)
    assert all(equal_urls)


def test_create_url_with_empty_urls():
    urls = []
    with pytest.raises(ValueError):
        create_url(urls=urls)


def test_create_url_with_not_dict_params():
    urls = ['https://test.com']
    params = ['name', 'client']
    with pytest.raises(TypeError):
        create_url(urls=urls, params=params)


def test_parse_json_response(
    sample_auth_response_200,
    sample_access_token_json_str
        ):
    parsed_json = parse_json_response(response=sample_auth_response_200)
    assert parsed_json == json.loads(sample_access_token_json_str)


def test_parse_json_response_no_json(sample_auth_response_404):
    with pytest.raises(InvalidJsonError):
        parse_json_response(sample_auth_response_404)
