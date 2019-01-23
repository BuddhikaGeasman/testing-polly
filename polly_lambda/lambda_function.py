mport boto3
import os
import urllib.parse
from contextlib import closing

polly = boto3.client('polly')
s3 = boto3.resource('s3')

def lambda_handler(event, context):
    output = os.environ['output']
    supported_languages = os.environ['supported_languages'].split('')
    default_language = os.environ['default_language']
    polly_bucket = os.environ['polly_bucket']
