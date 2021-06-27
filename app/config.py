import os
import sys
from pathlib import Path

import dotenv

from app.exceptions import InvalidConfigError

ENVIRONMENT = 'demo'

# postgresql+psycopg2://user:password@host:port/dbname[?key=value&key=value...]
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alena_kono:ak-test-PaSs@localhost/lamoda_oos'



class Config:
    ENV_CONFIG = {
        'production': '.env_prod',
        'demo': '.env_demo',
        'test': '.env_test',
        }
    ENV_VARS_NAMES = (
        'LAMODA_ENV_URL',
        'CLIENT_ID',
        'CLIENT_SECRET',
        'FLASK_SECRET_KEY',
    )

    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        env_info = self.environment or 'not set'
        return f'<{self.__class__.__name__} - {env_info}>'

    def _set_env(self, environment: str) -> None:
        if environment not in self.ENV_CONFIG:
            raise InvalidConfigError
        self.environment = environment

    def load_env(self, environment: str) -> None:
        self._set_env(environment)
        dotenv_path = self.ENV_CONFIG[self.environment]
        if not dotenv_path:
            raise FileNotFoundError('Dotenv_file is not found at current dir')
        dotenv.load_dotenv(dotenv_path=dotenv_path)

    def get(self) -> tuple:
        config = []
        for var_name in self.ENV_VARS_NAMES:
            var_value = os.environ.get(var_name)
            config.append(var_value)
        return tuple(config)


cfg = Config()
if 'pytest' not in sys.modules:
    cfg.load_env(ENVIRONMENT)
