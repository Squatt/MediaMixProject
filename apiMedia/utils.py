import json
import requests


def pretty_print(iterable):
    """Prints an iterable object with a newline after each element
    """
    for elem in iterable:
        print(elem)


def get_nouns(txt):
    """Returns a dict of all the nouns in a text and how often they appear.
    """
    query = 'https://api.textgain.com/1/tag?q='
    query += txt
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
    return nouns
