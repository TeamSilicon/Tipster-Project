from sentry_sdk.integrations.django import DjangoIntegration
import sentry_sdk
from iCrawl.settings.base import *
import os


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# For extra security --run python manage.py check --deploy
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True


ALLOWED_HOSTS = [".herokuapp.com"]


# SENTRY SETUP
SENTRY_KEY = os.getenv('SENTRY_KEY')
SENTRY_ORG = os.getenv('SENTRY_ORG')
SENTRY_PROJECT = os.getenv('SENTRY_PROJECT')

sentry_sdk.init(
    dsn=f"https://{SENTRY_KEY}@{SENTRY_ORG}.ingest.sentry.io/{SENTRY_PROJECT}",
    integrations=[DjangoIntegration()],

    # To associate users to errors
    send_default_pii=True
)

TODAY_FETCH_INTERVAL_MINS=7
YEST_FETCH_INTERVAL_MINS=60
TMRW_FETCH_INTERVAL_MINS=45