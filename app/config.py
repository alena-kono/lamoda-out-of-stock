import os

import dotenv

dotenv.load_dotenv()

# flask config
SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')

# lamoda environment config
LAMODA_ENV_PRODUCTION = True

if LAMODA_ENV_PRODUCTION:
    CLIENT_ID = os.environ.get('CLIENT_ID_PRODUCTION')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET_PRODUCTION')
    LAMODA_ENV_URL = 'https://api-b2b.lamoda.ru'
else:
    CLIENT_ID = os.environ.get('CLIENT_ID_DEMO')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET_DEMO')
    LAMODA_ENV_URL = 'https://api-demo-b2b.lamoda.ru'
