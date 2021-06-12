import os

import dotenv

from app.exceptions import InvalidConfigError

ENVIRONMENT = 'production'


class Config:
    ENV_CONFIG = {
        'production': '.env_prod',
        'demo': '.env_demo',
        'test': '.env_test',
        }

    def __init__(self, environment: str) -> None:
        if environment not in self.ENV_CONFIG:
            raise InvalidConfigError
        self.environment = environment

    def __repr__(self) -> str:
        return f'<Config - {self.environment}>'

    def load_env_vars(self) -> None:
        dotenv.load_dotenv(dotenv_path=self.ENV_CONFIG[self.environment])

    @staticmethod
    def _get_config_from_env_vars() -> tuple:
        SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
        CLIENT_ID = os.environ.get('CLIENT_ID')
        CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
        LAMODA_ENV_URL = os.environ.get('LAMODA_ENV_URL')
        return (LAMODA_ENV_URL, CLIENT_ID, CLIENT_SECRET, SECRET_KEY)

    def get_config(self) -> tuple:
        self.load_env_vars()
        return self._get_config_from_env_vars()


conf = Config(ENVIRONMENT)
