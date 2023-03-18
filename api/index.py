from flask import Flask, requests
from code.code import str_hello_world
from common.configs import get_configs
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
    folder = requests.args('folder')


# class handler(BaseHTTPRequestHandler):

#     def do_GET(self):
#         self.send_response(200)
#         self.send_header(200)
#         self.end_headers()
#         self.wfile.write(str_hello_world().encode('utf-8'))
#         return
