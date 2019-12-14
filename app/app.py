from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS, cross_origin
import time
import json
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/hello/<name>')
def hello_var(name):
    return "Hello, {}. How are you?".format(name)
    
if __name__ == '__main__':
   app.run()
