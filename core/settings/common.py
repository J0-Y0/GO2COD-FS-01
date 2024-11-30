from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Application definition

INSTALLED_APPS = [
    "unfold",  # before django.contrib.admin
    "unfold.contrib.filters",  # optional, if special filters are needed
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework_simplejwt",
    "djoser",
    "taggit",
    "mptt",
    "rest_framework",
    "rest_framework_nested",
    "drf_spectacular",
    "corsheaders",
    "blog",
    "authentication",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
UNFOLD = {
    "SITE_TITLE": "My Custom Admin Panel",  # Title suffix
    "SITE_HEADER": "JO Blog Admin",  # Sidebar header
    "SITE_URL": "",  # Redirect URL for the site header
    "SITE_SYMBOL": "speed",  # Symbol from the icon set
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/svg+xml",
            "href": lambda request: static("favicons/favicon.svg"),
        },
    ],
    "SHOW_HISTORY": True,  # Show "History" button
    "SHOW_VIEW_ON_SITE": True,  # Show "View on site" button
    "THEME": "dark",  # Force dark theme
    "COLORS": {
        "font": {
            "subtle-light": "107 114 128",
            "subtle-dark": "156 163 175",
            "default-light": "75 85 99",
            "default-dark": "209 213 219",
            "important-light": "17 24 39",
            "important-dark": "243 244 246",
        },
        "primary": {
            "50": "240 249 255",
            "100": "224 242 254",
            "200": "186 230 253",
            "300": "125 211 252",
            "400": "56 189 248",
            "500": "14 165 233",
            "600": "2 132 199",
            "700": "3 105 161",
            "800": "7 89 133",
            "900": "12 74 110",
            "950": "8 47 73",
        },
    },
    "SIDEBAR": {
        "show_search": True,  # Enable search in applications and models
        "show_all_applications": True,  # Show dropdown with all applications and models
        "navigation": [
            {
                "title": _("Content Management"),
                "separator": True,
                "collapsible": False,
                "items": [
                    {
                        "title": _("Posts"),
                        "icon": "article",
                        "link": reverse_lazy("admin:blog_post_changelist"),
                    },
                    {
                        "title": _("Comments"),
                        "icon": "comment",
                        "link": reverse_lazy("admin:blog_comment_changelist"),
                    },
                    {
                        "title": _("Reports"),
                        "icon": "report",
                        "link": reverse_lazy("admin:blog_report_changelist"),
                    },
                    {
                        "title": _("Categories"),
                        "icon": "category",  # Adjust icon based on preference
                        "link": reverse_lazy("admin:blog_category_changelist"),
                    },
                    {
                        "title": _("Tags"),
                        "icon": "tag",  # Adjust icon based on preference
                        "link": reverse_lazy(
                            "admin:taggit_tag_changelist"
                        ),  # For `TaggableManager`
                    },
                ],
            },
            {
                "title": _("User Management"),
                "separator": True,
                "collapsible": False,
                "items": [
                    {
                        "title": _("Users"),
                        "icon": "people",
                        "link": reverse_lazy("admin:authentication_user_changelist"),
                    },
                    {
                        "title": _("User Groupe"),
                        "icon": "partner_exchange",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                ],
            },
        ],
    },
}


REST_FRAMEWORK = {
    # "COERCE_DECIMAL_TO_STRING": False,
    # "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    # "PAGE_SIZE": 50,
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}


DJOSER = {
    "SERIALIZERS": {
        "user_create": "authentication.serializers.UserCreateSerializer",
        "current_user": "authentication.serializers.UserSerializer",
    }
}

AUTH_USER_MODEL = "authentication.User"

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
}
