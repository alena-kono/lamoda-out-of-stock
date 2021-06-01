import pytest

from app.utils import create_url, parse_json_response


@pytest.mark.parametrize('urls', [['https://test.com', '/auth/token'], []])
def test_create_url(urls):
    request_url = create_url(urls=urls)
    expected_request_url = 'https://test.com/auth/token'
    assert request_url == expected_request_url


def test_create_urls_with_empty_urls():
    urls = []
    with pytest.raises(TypeError):
        create_url(urls=urls)


@pytest.mark.skip(reason='empty test')
def test_parse_json_response():
    pass
