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
def search_box():
    return render_template('search.html')

@app.route('/search/', methods = ['POST'])
def search_string():
    value = request.form['val']
    ret = file_call(value)

    return jsonify(ret)

if __name__ == '__main__':
   app.run(debug = True)
