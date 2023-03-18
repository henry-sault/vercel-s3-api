import boto3
s3 = boto3.client('s3')


def str_hello_world() -> str:
    str = 'Hello, World!'
    return str


def list_s3_folder_contents(bucket: str, folder: str, path: str) -> list:
    object_list = s3.list_objects_v2(
        bucket=bucket,
        delimiter=path)
    key_array = []
    for vals in object_list:
        key_array.append(vals['Key'])
    return key_array
