from flask import Flask, request
from common.configs import get_configs
from common.code import list_s3_folder_contents

import os
import boto3

STAGE = os.getenv('STAGE', 'DEV')
CONFIGS = get_configs(STAGE)
s3 = boto3.client('s3')

app = Flask(__name__)


@app.route('/')
def home() -> str:
    return 'Hello, World!'


@app.route('/about')
def about() -> str:
    return 'Cren Cheddar'


@app.route('/sample-pictures')
def retrieve_pictures() -> list:
    folder_path = request.args.get('path')
    cloudfront_key_list = []
    photo_key_list = list_s3_folder_contents(
        CONFIGS['PHOTO_BUCKET'], folder_path)
    for key in photo_key_list:
        cloudfront_key_list.append(f'{CONFIGS["CLOUDFRONT_URL"]}/{key}')
    return cloudfront_key_list

# class handler(BaseHTTPRequestHandler):

#     def do_GET(self):
#         self.send_response(200)
#         self.send_header(200)
#         self.end_headers()
#         self.wfile.write(str_hello_world().encode('utf-8'))
#         return
