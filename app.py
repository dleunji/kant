from flask import Flask, request, render_template, jsonify, Response
import requests
#import gpt_2_simple as gpt2
import json
import os
from transformers import AutoTokenizer

autoTokenizer = AutoTokenizer.from_pretrained("gpt2-large")
# os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

app = Flask(__name__, static_url_path='/static')
# sess = gpt2.start_tf_sess()
# gpt2.load_gpt2(sess)


@app.route('/gpt2', methods=['POST'])
def gpt2():
    prefix = request.form['context']
    encodedText = autoTokenizer.encode(prefix)
    print(encodedText)
    headers = {'Content-Type' : 'application/json; charset=utf-8'}
    data = {
        'text' : encodedText,
        'length' : 200,
        'num_samples' : 1
    }
    url = "https://train-avgw7n5kbmsb7wrip2a8-gpt2-train-teachable-ainize.endpoint.dev.ainize.ai/predictions/gpt-2-en-small-finetune"
    response = requests.post(url, headers = headers, data = json.dumps(data))
    if response.status_code == 200:
        res = response.json()
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
