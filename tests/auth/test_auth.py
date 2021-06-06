import pytest
from app.auth.auth import Auth
from app.auth.exceptions import AccessTokenError


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


def test_get_auth_response(sample_auth, sample_auth_response_200):
    response = sample_auth._get_auth_response()
    response_expected = sample_auth_response_200
    assert response.status_code == response_expected.status_code
    assert response.url == response_expected.url
    assert response.headers == response_expected.headers

def test_set_auth_response(sample_auth, sample_auth_response_200):
    sample_auth._set_auth_response(sample_auth_response_200)
    assert sample_auth.response == sample_auth_response_200


def test_get_access_token(sample_auth, sample_auth_response_200):
    access_token = sample_auth._get_access_token()
    access_token_expected = sample_auth_response_200.json()['access_token']
    assert access_token == access_token_expected


def test_set_access_token(sample_auth, sample_auth_response_200):
    sample_auth._set_access_token()
    access_token_expected = sample_auth_response_200.json()['access_token']
    assert sample_auth.access_token == access_token_expected


def test_set_access_token_none_value(sample_auth, sample_auth_response_404):
    with pytest.raises(AccessTokenError):
        sample_auth._set_access_token()


def test_get_oauth2_headers(sample_auth, sample_auth_response_200):
    headers = sample_auth.get_oauth2_headers()
    headers_expected = {
        'Content-type': 'application/json',
        'Authorization': f'Bearer {sample_auth.access_token}',
        }
    assert headers == headers_expected
