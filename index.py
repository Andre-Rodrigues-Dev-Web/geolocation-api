#!/usr/bin/env python3

from collections import OrderedDict
import flask
from flask import Flask, request, Response, jsonify, render_template 
from flask_cors import CORS, cross_origin

import urllib.parse
import requests

app = flask.Flask(__name__)
app.config['DEBUG'] = False
key = "SUA_CHAVE" #locationiq.com
port = 81

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['get'])
def index():

    # -----------------------------------------------
    # Welcome
    # -----------------------------------------------
    return jsonify({"mensagem": "Acesso via /api/geocode?lat=-37.870662&lon=144.9803321"})

CORS(app, resources=r'/api/*')
@app.route('/api/geocode', methods=['GET'])
def geocode():

    # -----------------------------------------------
    # Example request POST
    # /geocode?lat=-37.870662&lon=144.9803321
    # -----------------------------------------------

    lat = request.args['lat']
    lon = request.args['lon']

    url = "https://us1.locationiq.com/v1/reverse.php?key="+key+"&lat="+lat+"&lon="+lon+"&format=json"
    response = requests.get(url)

    return response.json()

app.run(host="0.0.0.0", port=port)