from django.contrib.messages import constants
import dj_database_url

from pathlib import Path
import tomllib
import sys
import os


arq = open("env.toml", "rb")
toml_data = tomllib.load(arq)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, "../apps"))


SECRET_KEY = toml_data["secret_key"]

DEBUG = toml_data["debug"]

ALLOWED_HOSTS = toml_data["allowed_hosts"]
CSRF_TRUSTED_ORIGINS = toml_data["csrf_trusted_origins"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",  # WhiteNoise
    "django.contrib.staticfiles",
    # Libraries apss
    # My apps
    "authentication",
    "products",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
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
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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


# Database


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
    if DEBUG
    else {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": toml_data["database"]["name"],
        "USER": toml_data["database"]["user"],
        "PASSWORD": toml_data["database"]["password"],
        "HOST": toml_data["database"]["host"],
        "PORT": toml_data["database"]["port"],
    }
}

# Password validation

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

AUTH_USER_MODEL = "authentication.User"
AUTHENTICATION_BACKENDS = ("authentication.backends.CustomBackend",)


# Internationalization

LANGUAGE_CODE = "pt-BR"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "templates/static"), os.path.join(BASE_DIR, "media")]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Media files (Any arqs)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
WHITENOISE_AUTOREFRESH = True
WHITENOISE_USE_FINDERS = True


# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Messages

MESSAGE_TAGS = {
    constants.DEBUG: "alert-primary",
    constants.ERROR: "alert-danger",
    constants.SUCCESS: "alert-success",
    constants.INFO: "alert-info",
    constants.WARNING: "alert-warning",
}


# EFÍ checkout

if DEBUG:
    EFI_CREDENTIALS = {
        "client_id": toml_data["payments"]["homologacao"]["client_id"],
        "client_secret": toml_data["payments"]["homologacao"]["client_secret"],
        "sandbox": True,
        "certificate": os.path.join(
            BASE_DIR, toml_data["payments"]["homologacao"]["certificate"]
        ),
    }
else:
    EFI_CREDENTIALS = {
        "client_id": toml_data["payments"]["producao"]["client_id"],
        "client_secret": toml_data["payments"]["producao"]["client_secret"],
        "sandbox": False,
        "certificate": os.path.join(
            BASE_DIR, toml_data["payments"]["producao"]["certificate"]
        ),
    }
PIX_KEY = toml_data["payments"]["pix_key"]


arq.close()
