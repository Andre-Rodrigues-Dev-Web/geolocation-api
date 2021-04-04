#! /usr/bin/env python

from collections import OrderedDict
import flask
from flask import Flask, request, Response, jsonify, render_template 
import urllib.parse
import requests
from waitress import serve

app = flask.Flask(__name__)
app.config['DEBUG'] = True
key = "d6f49dee38b888"

@app.route('/geocode', methods=['GET'])
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

#app.run()
serve(app, host='0.0.0.0', port=80)