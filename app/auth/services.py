from typing import Dict

from app.auth.auth import Auth
from app.auth.exceptions import ClientCredentialsError
from app.config import cfg


def get_auth_headers() -> Dict[str, str]:
    credentials = cfg.get()[0:3]
    if all(credentials):
        a = Auth(*credentials)
        return a.get_oauth2_headers()
    raise ClientCredentialsError('Client credentials are missing')
