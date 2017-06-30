import os
import sys

from django.core.management import execute_from_command_line
from django.conf import settings

import urls


BASE_DIR = os.path.dirname(__file__)
BUILD_DIR = os.environ.get('BUILD_DIR', 'build')


settings.configure(
    DEBUG=True,
    SECRET_KEY='random_key',
    ROOT_URLCONF=urls,
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'django.contrib.contenttypes',
        'dh5bp'
    ),
    STATIC_URL='/static/',
    STATICFILES_DIRS=[
        os.path.join(BASE_DIR, 'static'),
    ],
    STATIC_ROOT=os.path.join(BUILD_DIR, 'static'),
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True
        }
    ],
)


if __name__ == '__main__':
    execute_from_command_line(sys.argv)
