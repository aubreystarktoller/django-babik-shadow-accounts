DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}

SECRET_KEY = "django_tests_secret_key"


TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'OPTIONS': {
        'context_processors': [
        ],
    },
}]

ROOT_URLCONF = 'tests.urls'

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'babik_shadow_accounts',
    'tests.testapp',
]

MIDDLEWARE_CLASSES = []

AUTH_USER_MODEL = 'testapp.CustomUser'
