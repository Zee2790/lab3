#!flask/bin/python
 

import time, os, sys
import inspect
from os import environ as env
#import shade
import lab3 as A
from flask import Flask, jsonify, render_template, request
import subprocess

app = Flask(__name__)

#### convert existing server to ansible_master api


@app.route('/lab3/api/tweet', methods=['GET'])
def getdata():
    A.mydata1()
    data = A.datadisplay()
    
    return jsonify(data)

@app.route('/lab3/api/data', methods=['GET'])
def getdata1():
    #A.mydata1()
    data=subprocess.check_output(["cowsay","Hello student"])
    return data

    

if __name__ == '__main__':
    
    app.run(host='0.0.0.0',debug=True)

