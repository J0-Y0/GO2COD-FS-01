from .common import *

DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


SECRET_KEY = "django-insecure-$@+)!ez+qhi39#^z1-l-8g06ct&noz$go16ekr@(#+h+8&3%(="
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]
SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=2),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=10),
}
SPECTACULAR_SETTINGS = {
    "TITLE": "JanPost API",
    "DESCRIPTION": "All the API endpoints for JanPost",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "EXTENSIONS_INFO": {
        "x-copyright": "© 2024 Yosef Emyayu. All rights reserved.",
        "x-repository-url": "https://github.com/J0-Y0/GO2COD-FS-01",
    },
    "CONTACT": {
        "name": "Yosef Emyayu",
        "url": "https://github.com/J0-Y0",
        "email": "yosef.emyayu1@gmail.com",
    },
}
