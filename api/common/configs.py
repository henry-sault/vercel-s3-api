import boto3
import os


def get_configs(STAGE) -> dict:
    ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID', 'DEV')
    SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', 'DEVSECRET')
    PHOTO_BUCKET = 'photography-albums'

    return {
        "AWS_ACCESS_KEY": ACCESS_KEY,
        "AWS_SECRET_ACCESS_KEY": SECRET_ACCESS_KEY,
        "PHOTO_BUCKET": PHOTO_BUCKET
    }
