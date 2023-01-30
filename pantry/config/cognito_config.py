from os import environ
from dotenv import load_dotenv

load_dotenv("./pantry/config/app-config.env")

TESTING = True
DEBUG = True

COGNITO_REGION = environ.get('COGNITO_REGION')
COGNITO_DOMAIN = environ.get('COGNITO_DOMAIN')
COGNITO_USER_POOL_ID = environ.get('COGNITO_USER_POOL_ID')
COGNITO_CLIENT_ID = environ.get('COGNITO_CLIENT_ID')
COGNITO_CLIENT_SECRET = environ.get('COGNITO_CLIENT_SECRET')
COGNITO_REDIRECT_URI = environ.get('COGNITO_REDIRECT_URL')
COGNITO_SIGNOUT_URI = environ.get('COGNITO_SIGNOUT_URL')
