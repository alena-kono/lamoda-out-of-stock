import requests
from app.auth.services import get_auth_headers


def test_get_auth_headers(sample_credentials, request_mocker, expected_oauth2_headers):
    LAMODA_ENV_URL, CLIENT_ID, CLIENT_SECRET = sample_credentials
    request_mocker.get(LAMODA_ENV_URL)
    requests.get(LAMODA_ENV_URL)
    headers = get_auth_headers()
    assert headers == expected_oauth2_headers
