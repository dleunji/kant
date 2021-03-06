from flask import Flask, request, render_template, jsonify, Response
import requests
import gpt_2_simple as gpt2
import json
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

app = Flask(__name__, static_url_path='/static')
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        prefix = request.form['prefix']
        if prefix == "":
            return render_template('index.html', result=None)
        essay = gpt2.generate(sess,
                              prefix=prefix, length=150, return_as_list=True)[0]
        print(essay)
        data = {"essay": essay}
        return render_template('index.html', result=data)
    else:
        return render_template('index.html', result=None)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
