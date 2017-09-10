#!/usr/bin/env python3

import json

from apiMedia.FluxRSS.imports.Server_IMPORTS import *
from apiMedia.FluxRSS.FluxRSSManager import *
from apiMedia.RSSParser import LeMondeParser, MediaPartParser
from apiMedia.utils import get_nouns

app = Flask(__name__)


parsers = [
    LeMondeParser,
    MediaPartParser,
]

def get_titles():
    titles = []
    for parser in parsers:
        titles.extend(parser().get_titles())
    text = ' '.join(titles)
    return json.dumps(titles) + json.dumps(get_nouns(text))

## Route flux RSS Manager ##
app.add_url_rule('/getActualities', 'getActualities',
                 get_titles, methods=['GET'])


def start():
    app.run(host='0.0.0.0', port=4242)
