# settings_dast.py - TYLKO dla DAST CI
from .settings import *

# WYŁĄCZ HTTPS całkowicie
SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = None
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = 0

DEBUG = True
ALLOWED_HOSTS = ['*', 'localhost', '127.0.0.1']

CSRF_TRUSTED_ORIGINS = ['http://localhost:8000', 'http://127.0.0.1:8000']
