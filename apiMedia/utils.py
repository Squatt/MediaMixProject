# MIT License
#
# Copyright (c) 2017 Ludovic Mandagot, Luka Peschke
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# @author Luka Peschke
#


import json
import requests
import re
import urllib.parse


def pretty_print(iterable):
    """Prints an iterable object with a newline after each element
    """
    for elem in iterable:
        print(elem)


def get_nouns(txt):
    """Returns a dict of all the nouns in a text and how often they appear.
    """
    query = 'https://api.textgain.com/1/tag?q='
    query += urllib.parse.quote(txt, safe='')
    query += '&lang=fr&key=***'
    resp = requests.get(query)

    body = json.loads(resp.text)['text'][0]

    nouns = {}
    for iterable_elem in body:
        for elem in iterable_elem:
            if elem['tag'] == 'NOUN':
                word = elem['word']
                if word in nouns.keys():
                    nouns[word] += 1
                else:
                    nouns[word] = 1
    print(nouns)
    return nouns


def dirty_yt_search(keyword):
    """Searches for the specified keyword on YouTube and returns the first
    video result.
    """
    yt_url = 'https://www.youtube.com/results'
    search_args = {'search_query': keyword}

    resp = requests.get(yt_url, search_args)
    print(resp.text)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', resp.text)
    return 'http://www.youtube.com/watch?v=' + search_results[0]
