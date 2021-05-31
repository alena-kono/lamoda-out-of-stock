import pytest
import requests
from collections import namedtuple
import requests_mock

from app.auth.auth import Auth
from app.utils import create_url
from app.auth.exceptions import AccessTokenError


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
def request_mocker():
    with requests_mock.Mocker() as request_mocker:
        yield request_mocker


def test_init(sample_auth, sample_credentials):
    auth = Auth(*sample_credentials)
    assert sample_auth.domain_url == auth.domain_url
    assert sample_auth.client_id == auth.client_id
    assert sample_auth.client_secret == auth.client_secret


def test_get_request_params(sample_auth, sample_credentials):
    request_params = sample_auth._get_request_params()
    request_params_expected = {
        'client_id': sample_credentials.client_id,
        'client_secret': sample_credentials.client_secret,
        'grant_type': 'client_credentials',
        }
    assert request_params == request_params_expected


def test_get_auth_response(request_mocker, sample_auth, sample_auth_token_url):
    request_mocker.get(sample_auth_token_url)
    response = sample_auth._get_auth_response()
    response_expected = requests.get(sample_auth_token_url)
    assert response.status_code == response_expected.status_code
    assert response.url == response_expected.url
    assert response.headers == response_expected.headers


def test_get_access_token(request_mocker, sample_auth, sample_auth_token_url, sample_access_token_json):
    request_mocker.get(sample_auth_token_url, json=sample_access_token_json)
    response = sample_auth._get_auth_response()
    access_token = sample_auth._get_access_token(response)
    access_token_expected = sample_access_token_json['access_token']
    assert access_token == access_token_expected


def test_set_access_token(request_mocker, sample_auth, sample_auth_token_url, sample_access_token_json):
    request_mocker.get(sample_auth_token_url, json=sample_access_token_json)
    response = sample_auth._get_auth_response()
    sample_auth._set_access_token(response)
    token_expected = sample_access_token_json['access_token']
    assert sample_auth.access_token == token_expected


def test_set_access_token_none_value(request_mocker, sample_auth, sample_auth_token_url, sample_access_token_json):
    request_mocker.get(sample_auth_token_url, status_code=404, json=sample_access_token_json)
    response = sample_auth._get_auth_response()
    with pytest.raises(AccessTokenError):
        sample_auth._set_access_token(response)
