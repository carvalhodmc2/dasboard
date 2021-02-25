from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class Secrets:
    SECRET_KEY = 'django'
    DEBUG = True
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

    DATABASE_URL = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
