import json

import pytest
import requests
import requests_mock
from app.exceptions import NoJsonError
from app.utils import create_url, parse_json_response


@pytest.fixture
def expected_urls():
    urls_with_dict_params = {
        'https://test.com/auth/token?client_id=42&name=Best-Client': {
            'urls': ['https://test.com', '/auth/token'],
            'params': {'client_id': '42', 'name': 'Best-Client'}
            },
        'https://test.com': {'urls': ['https://test.com']},
        'https://test.com10': {'urls': ['https://test.com', 10]},
    }
    return urls_with_dict_params


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


@pytest.fixture
def sample_json():
    sample_json = '{"page":"1", "limit":"1000000", "_links": []}'
    return json.loads(sample_json)


@pytest.fixture
def sample_response_with_valid_json(sample_json):
    url = 'https://test.com'
    with requests_mock.Mocker() as request_mocker:
        request_mocker.get(url, json=sample_json)
        return requests.get(url)


@pytest.fixture
def sample_response_with_no_json():
    url = 'https://test.com'
    with requests_mock.Mocker() as request_mocker:
        request_mocker.get(url)
        return requests.get(url)


def test_parse_json_response(sample_response_with_valid_json):
    parsed_json = parse_json_response(response=sample_response_with_valid_json)
    expected_json = {
        "page": "1",
        "limit": "1000000",
        "_links": [],
        }
    assert parsed_json == expected_json


def test_parse_json_response_no_json(sample_response_with_no_json):
    with pytest.raises(NoJsonError):
        parse_json_response(sample_response_with_no_json)
