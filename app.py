from flask import Flask, request, render_template, jsonify, Response
import requests
import json
import os
from transformers import AutoTokenizer

autoTokenizer = AutoTokenizer.from_pretrained("gpt2-large")

app = Flask(__name__, static_url_path='/static')

@app.route('/gpt2', methods=['POST'])
def gpt2():
    prefix = request.form['context']
    encodedText = autoTokenizer.encode(prefix)
    print(encodedText)
    headers = {'Content-Type' : 'application/json; charset=utf-8'}
    data = {
        'text' : encodedText,
        'length' : 200
    }
    url = "https://train-avgw7n5kbmsb7wrip2a8-gpt2-train-teachable-ainize.endpoint.dev.ainize.ai/predictions/gpt-2-en-small-finetune"
    response = requests.post(url, headers = headers, data = json.dumps(data))
    if response.status_code == 200:
        res = response.json()
        print(res[0])
        text = autoTokenizer.decode(res[0], skip_special_tokens=True)
        print(text)
        return jsonify({'text' : text}), 200
    else:
        return jsonify({'fail' : 'eror'}), response.status_code

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
