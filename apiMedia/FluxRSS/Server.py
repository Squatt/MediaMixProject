#!/usr/bin/env python3

import json

from apiMedia.FluxRSS.imports.Server_IMPORTS import *
from apiMedia.FluxRSS.FluxRSSManager import *
from apiMedia.RSSParser import LeMondeParser, MediaPartParser, ExpressParser, LeParisienParser, RadioCanadaParser
from apiMedia.utils import get_nouns, dirty_yt_search

app = Flask(__name__)


parsers = [
    LeMondeParser,
    LeParisienParser,
    RadioCanadaParser,
]

def get_hottest_noun(nouns={}):
    highest = 0
    noun = None
    for k, v in nouns.items():
        if v > highest and len(k) > 2:
            highest = v
            noun = k
    return noun

def get_titles():
    titles = []
    for parser in parsers:
        titles.extend(parser().get_titles())
    text = ' '.join(titles)
    nouns = get_nouns(text)
    hot = get_hottest_noun(nouns) + " " + 'actualité')
    print(hot);
    return hot + " : " + dirty_yt_search(hot if hot else 'toto')


## Route flux RSS Manager ##
app.add_url_rule('/getActualities', 'getActualities',
                 get_titles, methods=['GET'])


def start():
    app.run(host='0.0.0.0', port=4242)
