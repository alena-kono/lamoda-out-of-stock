import json
from collections import namedtuple

import pytest
import requests
import requests_mock
from app.auth.auth import Auth
from app.config import Config, conf
from app.utils import create_url


@pytest.fixture(scope='session', autouse=True)
def tests_setup_and_teardown():
    Config('test').load_env_vars()
    yield


def test_config_is_equal(sample_credentials, sample_auth_response_200):
    assert sample_credentials.domain_url == conf.get_config()[0]


@pytest.fixture
def sample_credentials():
    Auth_credentials = namedtuple(
        'Auth_credentials', ['domain_url', 'client_id', 'client_secret']
        )
    sample_credentials = Auth_credentials(
        domain_url='https://test.com',
        client_id='qwerty123456',
        client_secret='some_secret_words',
        )
    return sample_credentials


@pytest.fixture
def sample_auth(sample_credentials):
    auth = Auth(*sample_credentials)
    return auth


@pytest.fixture
def sample_auth_token_url(sample_credentials):
    url_parts = [sample_credentials.domain_url, '/auth/token']
    params = {
        'client_id': sample_credentials.client_id,
        'client_secret': sample_credentials.client_secret,
        'grant_type': 'client_credentials',
        }
    return create_url(url_parts, params)


@pytest.fixture
def sample_access_token_json():
    return {
        'access_token': 'GREAT_great_token_EvEr5',
        'expires_in': 1200,
        'token_type': 'string',
        'scope': 'string'
        }


@pytest.fixture
def sample_access_token_json_str(sample_access_token_json):
    return json.dumps(sample_access_token_json)


@pytest.fixture
def request_mocker():
    with requests_mock.Mocker() as request_mocker:
        yield request_mocker


@pytest.fixture
def sample_auth_response_200(
    request_mocker,
    sample_auth_token_url,
    sample_access_token_json
        ):
    request_mocker.get(sample_auth_token_url, json=sample_access_token_json)
    return requests.get(sample_auth_token_url)


@pytest.fixture
def sample_auth_response_404(request_mocker, sample_auth_token_url):
    request_mocker.get(sample_auth_token_url, status_code=404)
    return requests.get(sample_auth_token_url)


@pytest.fixture
def expected_oauth2_headers(sample_access_token_json):
    access_token = sample_access_token_json['access_token']
    return {
        'Content-type': 'application/json',
        'Authorization': f'Bearer {access_token}',
        }


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
