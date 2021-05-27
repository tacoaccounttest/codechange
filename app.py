import logging
import argparse
from flask import Flask, render_template, jsonify, request
from datetime import datetime

from registration import Registration
from registrator import Registrator
from configuration import Configuration

from myservice import myservice


# default config file (use -c parameter on command line specify a custom config file)
configfile = "app.conf"

# endpoint for Web page containing information about the service
aboutendpoint = "/about"

# endpoint for health information of the service required for Spring Boot Admin server callback
healthendpoint = "/health"


# initialize Flask app and add the externalized service information
app = Flask(__name__)
app.register_blueprint(myservice)

# holds the configuration
configuration = None


@app.route(healthendpoint, methods=['GET'])
def health():
    """required health endpoint for callback of Spring Boot Admin server"""
    return "alive"

 