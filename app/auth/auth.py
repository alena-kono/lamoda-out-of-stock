from typing import Dict, NoReturn, Optional

import requests
from app.auth.exceptions import AccessTokenError
from app.utils import create_url


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

    def _get_auth_response(self) -> requests.Response:
        url_parts = [self.domain_url, '/auth/token']
        params = self._get_request_params()
        request_url = create_url(url_parts, params)
        return requests.get(request_url)

    def _get_access_token(response: requests.Response) -> Optional[str]:
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
