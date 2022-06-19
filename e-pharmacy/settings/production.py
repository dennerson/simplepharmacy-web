from .base import *

DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = ['ip-address', 'www.your-website.com']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': ''
    }
}

#
STRIPE_PUBLIC_KEY = "pk_test_51L0TVPEBFQU6SztAEgiuyiBek4ULIux0K3NzrZB9YGK1oNhS1m0FXcA7ujJq7lNAvQ1SAtjZOCJyDBDaLGnaS3LL00RQRMZOrz"
# config('STRIPE_LIVE_PUBLIC_KEY')
# "pk_test_51L0TVPEBFQU6SztAEgiuyiBek4ULIux0K3NzrZB9YGK1oNhS1m0FXcA7ujJq7lNAvQ1SAtjZOCJyDBDaLGnaS3LL00RQRMZOrz"
#
STRIPE_SECRET_KEY = "sk_test_51L0TVPEBFQU6SztABJz8XX1xxON0T5jNXr1b6LJKAyyyws0QZYHYp9x7WWzQTHotkFBvNPbGWA7DhCkwIa6tJ7D000oVtoiwT5"
# config('STRIPE_LIVE_SECRET_KEY')
# "sk_test_51L0TVPEBFQU6SztABJz8XX1xxON0T5jNXr1b6LJKAyyyws0QZYHYp9x7WWzQTHotkFBvNPbGWA7DhCkwla6tJ7D000oVtoiwT5"
