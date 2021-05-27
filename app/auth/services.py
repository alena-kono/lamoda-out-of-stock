from typing import Dict

from app.auth.auth import Auth
from app.config import CLIENT_ID, CLIENT_SECRET, LAMODA_ENV_URL


def get_auth_headers() -> Dict[str]:
    url = LAMODA_ENV_URL
    a = Auth(url, CLIENT_ID, CLIENT_SECRET)
    return a.get_oauth2_headers()
