import pytest
from app.auth.exceptions import ClientCredentialsError
from app.auth.services import get_auth_headers


def test_get_auth_headers(expected_oauth2_headers, sample_auth_response_200):
    headers = get_auth_headers()
    assert headers == expected_oauth2_headers


def test_get_auth_headers_with_missing_credentials(
    sample_auth_response_200,
    missing_env_vars
        ):
    with pytest.raises(ClientCredentialsError):
        get_auth_headers()
