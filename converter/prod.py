import os

SECRET_KEY = 'django-insecure-s*4w!^f5_*!6mjm4lo%%29+*w@&^9!s(#29v2#9ebh9v&d11bu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# STATIC_ROOT = 'static'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
