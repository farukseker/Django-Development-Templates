from .base import *

CORS_ALLOW_ALL_ORIGINS = True
DEBUG = True


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
]

from storages.backends.s3boto3 import S3Boto3Storage

# AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
# AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
# AWS_S3_ENDPOINT_URL = env("AWS_S3_ENDPOINT_URL")  # MinIO's endpoint URL
# AWS_S3_ADDRESSING_STYLE = env("AWS_S3_ADDRESSING_STYLE")
# AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME")


AWS_ACCESS_KEY_ID="admin"
AWS_SECRET_ACCESS_KEY="supersecret"
AWS_STORAGE_BUCKET_NAME="my-bucket"
# AWS_S3_ENDPOINT_URL=http://localhost:9000
AWS_S3_ENDPOINT_URL="http://minio:9000"
AWS_S3_ADDRESSING_STYLE="path"
AWS_S3_CUSTOM_DOMAIN = f"{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}"



DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# STORAGES = {  # -- ADDED IN Django 5.1
#     "default": {
#         "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
#     },
#     "staticfiles": {
#         "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
#     },
# }

# MinIO-specific settings
MEDIA_URL = f"{AWS_S3_CUSTOM_DOMAIN}/media/"


STATIC_URL = f"http://localhost:9000/my-bucket/"
# STATIC_URL = "/static/"



# MinIO'ya yüklenmesi gereken dosyaların toplama ayarları
STATICFILES_DIRS = [BASE_DIR / 'static']

# STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles/'

# TEST 

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

s3 = boto3.client(
    's3',
    endpoint_url=AWS_S3_ENDPOINT_URL,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name='us-east-1',  # MinIO'nun desteklediği bir bölgeyi seçin
    config=boto3.session.Config(signature_version='s3v4')
)

try:
    response = s3.list_objects(Bucket=AWS_STORAGE_BUCKET_NAME)
    print(response)
except (NoCredentialsError, PartialCredentialsError) as e:
    print(f"Credential error: {e}")
except Exception as e:
    print(f"Error occurred: {e}")





SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True

from django.contrib.staticfiles.storage import staticfiles_storage
print(staticfiles_storage.url("admin/css/base.css"))


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'graylog': {
            'level': 'ERROR',
            'class': 'logging.handlers.DatagramHandler',
            'host': 'localhost',
            'port': 12201,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['graylog'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}