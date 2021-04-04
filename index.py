#! /usr/bin/env python

from collections import OrderedDict
import flask
from flask import Flask, request, Response, jsonify, render_template 
import urllib.parse
import requests

app = flask.Flask(__name__)
app.config['DEBUG'] = True
key = "d6f49dee38b888"

@app.route('/geocode', methods=['POST'])
def geocode():

    # -----------------------------------------------
    # Example request POST
    # /geocode?lat=-37.870662&lon=144.9803321
    # -----------------------------------------------

    lat = request.args['lat']
    lon = request.args['lon']

    url = "https://us1.locationiq.com/v1/reverse.php?key="+key+"&lat="+lat+"&lon="+lon+"&format=json"
    response = requests.post(url)

    return response.json()

app.run()