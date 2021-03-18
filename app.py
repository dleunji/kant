from flask import Flask, request, render_template, jsonify, Response
"""from transformers import AutoTokenizer"""
import requests
import gpt_2_simple as gpt2
import json
import os
app = Flask(__name__, static_url_path='/static')

model_name = "/checkpoint/run1"
sess = gpt2.start_tf_sess()


@app.route('/')
def main():
    return render_template("index.html")


# @app.route('/gpt2', methods=['POST'])
# def gpt2():
