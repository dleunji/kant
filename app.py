from flask import Flask, request, render_template, jsonify, Response
import requests
#import gpt_2_simple as gpt2
import json
import os
# os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

app = Flask(__name__, static_url_path='/static')
# sess = gpt2.start_tf_sess()
# gpt2.load_gpt2(sess)


@app.route('/gpt2', methods=['POST'])
def gpt2():
    prefix = request.form['context']
    print(prefix)
    if prefix == "":
        # 입력하라는 메세지 추가
        return render_template('index.html', result = None)
    else:
        text = prefix
        url = "https://kubecon-tabtab-ainize-team.endpoint.ainize.ai/url"
        for i in range(5):
            start = prefix
            data = {
                'context' : start,
                'length' : 'long',
                'model' : 'https://train-avgw7n5kbmsb7wrip2a8-gpt2-train-teachable-ainize.endpoint.dev.ainize.ai/predictions/gpt-2-en-small-finetune'
            }
            response = requests.post(url, data = data)
            res = response.json()
            text += res['0']
            prefix = res['0']
        print(res)
        print(text)
        return jsonify({'text' : text}), 200
    # if prefix == "":
    #     return render_template('index.html', result=None)
    # essay = gpt2.generate(sess,
    #                       prefix=prefix, length=150, return_as_list=True)[0]
    # print(essay)
    # data = {"essay": essay}
    # return render_template('index.html', result=data)

@app.route('/', methods=['GET'])
def main():
    if request.method == 'GET':
        return render_template('index.html', result=None)
    else : 
        return render_template('index.html', result=None)



if __name__ == '__main__':
    app.run(host="0.0.0.0")
