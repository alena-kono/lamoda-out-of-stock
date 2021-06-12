from app.auth.services import get_auth_headers


def test_get_auth_headers(expected_oauth2_headers, sample_auth_response_200):
    headers = get_auth_headers()
    assert headers == expected_oauth2_headers
