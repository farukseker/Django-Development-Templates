import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from storages.backends.s3boto3 import S3Boto3Storage
from pathlib import Path
import environ


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Take environment variables from .env file
env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')


AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
# AWS_S3_ENDPOINT_URL = env("AWS_S3_ENDPOINT_URL")  # MinIO's endpoint URL
AWS_S3_ENDPOINT_URL = "http://minio:9000"  # MinIO's endpoint URL
AWS_S3_ADDRESSING_STYLE = env("AWS_S3_ADDRESSING_STYLE")



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
