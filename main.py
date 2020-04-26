from flask import Flask
from flask import request

# from model_lstm import predict
from lstm_test import lstm_predict as predict
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

@app.route('/')
def main_page():
    return "<h1>It is running</h1>"