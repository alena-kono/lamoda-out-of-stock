from typing import Dict, NoReturn, Optional

import requests
from app.auth.exceptions import AccessTokenError

from app.config import CLIENT_ID, CLIENT_SECRET


class Auth:
    def __init__(self, url: str, client_id: str, client_secret: str) -> None:
        self.url = url
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = ''

    def _get_request_params(self) -> Dict[str, str]:
        return {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials',
            }

    def _get_access_token(self) -> Optional[str]:
        token_url = ''.join((self.url, '/auth/token'))
        params = self._get_request_params()
        response = requests.get(token_url, params=params)
        if response.status_code == 200:
            return str(response.json().get('access_token'))
        return None

    def _set_access_token(self) -> Optional[NoReturn]:
        if access_token := self._get_access_token():
            self.access_token = access_token
            return None
        raise AccessTokenError('Access token is missing')

    def get_oauth2_headers(self) -> Dict[str, str]:
        self._set_access_token()
        return {
            'Content-type': 'application/json',
            'Authorization': f'Bearer {self.access_token}'
            }


def get_auth_headers():
    URL = 'https://api-demo-b2b.lamoda.ru'
    a = Auth(URL, CLIENT_ID, CLIENT_SECRET)
    return a.get_oauth2_headers()
