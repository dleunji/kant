from flask import Flask
from transformers import AutoTokenizer
import json
import os

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def hello_world():
    return 'hello, Docker'
