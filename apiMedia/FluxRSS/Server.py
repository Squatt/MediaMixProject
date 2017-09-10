#!/usr/bin/python3
#-*- coding: utf-8 -*-

from imports.Server_IMPORTS import *
from FluxRSSManager import *

app = Flask(__name__)

## Route flux RSS Manager ##
app.add_url_rule('/getActualities', 'getActualities', GetActualities, methods=['GET'])


def start():
    app.run(host='0.0.0.0', port=4242)
