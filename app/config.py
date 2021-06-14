import os
import sys

import dotenv

from app.exceptions import InvalidConfigError

ENVIRONMENT = 'production'


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
        dotenv.load_dotenv(dotenv_path=self.ENV_CONFIG[self.environment])

    def get_config(self) -> tuple:
        config = []
        for var_name in self.ENV_VARS_NAMES:
            var_value = os.environ.get(var_name)
            config.append(var_value)
        return tuple(config)


cfg = Config()
if 'pytest' not in sys.modules:
    cfg.load_env(ENVIRONMENT)
