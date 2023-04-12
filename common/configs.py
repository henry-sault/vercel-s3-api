import boto3
import os

sts = boto3.client('sts')
role_creds = sts.assume_role(
    RoleArn=os.get_env("AWS_ROLE_ARN"), RoleSessionName='test_role')
print(f"access key id: {role_creds['Credentials']['AccessKeyId']}")


def get_configs(STAGE):
    ACCESS_KEY = role_creds['Credentials']['AccessKeyId']
    SECRET_ACCESS_KEY = role_creds['Credentials']['SecretAccessKey']
    SESSION_TOKEN = role_creds['Credentials']['SessionToken']
    PHOTO_BUCKET = 'photography-albums'
    PHOTO_PATH = 'testing/sample-images/'
    CLOUDFRONT_URL = 'dhhw3lfxwyceg.cloudfront.net'

    return {
        "AWS_ACCESS_KEY": ACCESS_KEY,
        "AWS_SECRET_ACCESS_KEY": SECRET_ACCESS_KEY,
        "PHOTO_BUCKET": PHOTO_BUCKET,
        "SESSION_TOKEN": SESSION_TOKEN,
        "PHOTO_PATH": PHOTO_PATH,
        "CLOUDFRONT_URL": CLOUDFRONT_URL
    }
