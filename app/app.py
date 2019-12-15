from flask import Flask, render_template
from flask import jsonify
from flask import request
from flask_cors import CORS, cross_origin
import time
import json
import requests
from parser import file_call

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/hello/<name>')
def hello_var(name):
    return render_template('test.html', name = name)

@app.route('/search/<value>')
def search_string(value):
    ret = file_call(value)

    return jsonify(ret)

# @app.route('/result', methods=['GET', 'POST'])
# def search_result():
#     temp = request.get_json()
#     return request.form['tosend']

if __name__ == '__main__':
   app.run(debug = True)
