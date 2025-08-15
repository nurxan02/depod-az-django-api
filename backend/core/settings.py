import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'dev-secret-key-change-me')

DEBUG = os.getenv('DJANGO_DEBUG', 'true').lower() == 'true'

ALLOWED_HOSTS = [h.strip() for h in os.getenv('DJANGO_ALLOWED_HOSTS', '*').split(',')]

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party
    'rest_framework',
    'corsheaders',

    # local apps
    'catalog',
    'sitecontent.apps.SitecontentConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

templates_dir = BASE_DIR / 'templates'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [templates_dir],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'
ASGI_APPLICATION = 'core.asgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'depod'),
        'USER': os.getenv('POSTGRES_USER', 'depod'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'depod'),
        'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
        'PORT': int(os.getenv('POSTGRES_PORT', '5432')),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'az'
TIME_ZONE = 'Asia/Baku'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.getenv('DJANGO_STATIC_ROOT', str(BASE_DIR / 'staticfiles'))
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = os.getenv('DJANGO_MEDIA_ROOT', str(BASE_DIR / 'media'))

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_ALL_ORIGINS = os.getenv('CORS_ALLOW_ALL', 'true').lower() == 'true'
CORS_ALLOWED_ORIGINS = [
    o.strip() for o in os.getenv('CORS_ALLOWED_ORIGINS', '').split(',') if o.strip()
]
CORS_ALLOW_CREDENTIALS = True

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}

# Jazzmin configuration (optional branding)
JAZZMIN_SETTINGS = {
    "site_title": "Depod Admin",
    "site_header": "Depod Admin",
    "site_brand": "Depod.az Admin",
    "welcome_sign": "Depod idarə panelinə xoş gəldiniz",
    # Logos (served from STATICFILES_DIRS)
    "site_logo": "img/logo.png",
    "login_logo": "img/logo.png",
    "custom_css": "css/admin-overrides.css",
    "custom_js": "js/admin-overrides.js",
    "copyright": "Depod. Developed by Masimzada",
    "show_ui_builder": False,
    # Reorder apps & models in sidebar
    "order_with_respect_to": [
        "catalog.Category",
        "catalog.Product",
        # Then our site personalisation section
        "sitecontent.AboutPageProxy",
        "sitecontent.ContactPageProxy",
        "sitecontent.FooterSettingsProxy",
    ],
    # Hide originals (we expose proxies under Site personalisation)
    "hide_models": [
        "catalog.AboutPage",
        "catalog.ContactPage",
        "catalog.FooterSettings",
    ],
    # Icons for apps/models
    "icons": {
        "catalog": "fas fa-boxes-stacked",
        "catalog.category": "fas fa-list",
        "catalog.product": "fas fa-box",
        "sitecontent": "fas fa-sitemap",
        "sitecontent.aboutpageproxy": "fas fa-info-circle",
        "sitecontent.contactpageproxy": "fas fa-address-book",
        "sitecontent.footersettingsproxy": "fas fa-shoe-prints",
    },

}
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": True,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-warning",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "lumen",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}
# WhiteNoise for static files in production
if not DEBUG:
    STORAGES = {
        'staticfiles': {
            'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
        },
    }
