from typing import Dict, NoReturn, Optional

import requests
from app.auth.exceptions import AccessTokenError

from app.config import CLIENT_ID, CLIENT_SECRET, LAMODA_ENV_URL


class Auth:
    def __init__(
        self, domain_url: str, client_id: str, client_secret: str
            ) -> None:
        self.domain_url = domain_url
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
        request_url = ''.join((self.domain_url, '/auth/token'))
        params = self._get_request_params()
        response = requests.get(request_url, params=params)
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
    url = LAMODA_ENV_URL
    a = Auth(url, CLIENT_ID, CLIENT_SECRET)
    return a.get_oauth2_headers()
