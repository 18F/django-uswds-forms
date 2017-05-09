import os
import pytest


APP_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


# Minimum settings required for the app's tests.
SETTINGS_DICT = {
    'BASE_DIR': APP_DIR,
    'INSTALLED_APPS': (
        'uswds_forms',
    ),
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(APP_DIR, 'db.sqlite3'),
        },
    },
    'MIDDLEWARE_CLASSES': (
        'django.middleware.common.CommonMiddleware',
    ),
    'TEMPLATES': [{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [],
        },
    }],
}


@pytest.fixture(scope="session", autouse=True)
def init_django():
    # Making Django run this way is a two-step process. First, call
    # settings.configure() to give Django settings to work with:
    from django.conf import settings
    settings.configure(**SETTINGS_DICT)

    # Then, call django.setup() to initialize the application cache
    # and other bits:
    import django
    django.setup()
