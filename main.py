from flask import Flask,render_template,request,url_for
import requests
from urllib.request import urlopen
import html5lib
import json
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def predict():
    if request.method == 'POST':
        comment = request.form['comment']
        #print(type(comment))
        api_url = "https://api.icndb.com/jokes/"+str(comment)
        url_result = urlopen(api_url)
        data = url_result.read()
        json_data = json.loads(data)
        joke = json_data['value']['joke']

    return render_template("results.html", comment=joke, id=comment)

if __name__ == '__main__':
    app.run(host="127.0.0.1",port=8080,debug=True)
