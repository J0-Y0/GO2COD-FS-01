import os
from .common import *
from dotenv import load_dotenv

load_dotenv()
DEBUG = True
ALLOWED_HOSTS = [
    str(os.getenv("ALLOWED_HOSTS")),
]

print("============", ALLOWED_HOSTS)
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY = os.getenv("SECRET_KEY")
# replace with production  database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DBNAME"),  # Replace with your database name
        "USER": os.getenv("DBUSER"),  # Replace with your database user
        "PASSWORD": os.getenv("DBPASSWORD"),  # Replace with your database password
        "HOST": os.getenv("DBHOST"),  # Replace with your database host
        "PORT": os.getenv("5432"),  # Optional: Specify the port
    }
}
CORS_ALLOWED_ORIGINS = [os.getenv("ALLOWED_ORIGINS")]
SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=3),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=6),
}
SPECTACULAR_SETTINGS = {
    "TITLE": "JanPost API",
    "DESCRIPTION": "All the API endpoints for JanPost",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SCHEMA_PATH_PREFIX": r"/api/v[0-9]",
    "SERVE_PERMISSIONS": ["rest_framework.permissions.IsAdminUser"],
    "COMPONENT_SPLIT_REQUEST": True,
    "SORT_OPERATIONS": True,
    "POSTPROCESSING_HOOKS": ["janpost.api_hooks.custom_postprocess"],
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
