import os

import dotenv

dotenv.load_dotenv()

# flask config
SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')

# lamoda credentials
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
