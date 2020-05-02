from flask import Flask
from flask import request

import pandas as pd

from src.lstm_test import lstm_predict as predict
from src import wordcount 
app = Flask("lstm_api")

@app.route('/api/predict/',methods=['POST'])
def post_predict():
    if request.method == 'POST':
        text = request.form['text']
        ret = predict(text)
        return {
            "text":text,
            "result":ret,
        }

@app.route("/api/wordcount/", methods=['POST'])
def post_wordcount():
    if request.method == 'POST':
        try:
            rettop = int(request.form.get("top"))
            print(type(rettop))
            if rettop <= 0:
                rettop = -1
        except KeyError:
            rettop = -1
        data = request.form.getlist("texts")
        # print(data)
        if type(data) is str:
            data = [data]
        
        if type(data) is list:
            data = pd.DataFrame({"comment": data})
            data = wordcount.split(data)
            data = wordcount.wordcount(data)
            if rettop != -1:
                data = data[:rettop]
            return data.to_dict()
        else:
            return {
                "error": "wrong type of text"
            }

@app.route('/')
def main_page():
    return "<h1>It is running</h1>"