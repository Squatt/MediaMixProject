#!/usr/bin/env python3

from sys import argv

import feedparser


def pretty_print(iterable):
    for elem in iterable:
        print(elem)

def get_raw_rss(url):
    return feedparser.parse(url)


def get_titles(raw_content):
    entries = raw_content.get('entries')
    if not entries:
        return []

    titles = []
    for entry in entries:
        titles.append(entry['title'])
    return titles


url = argv[1] if len(argv) > 1 else 'http://www.lemonde.fr/rss/une.xml'
titles = get_titles(get_raw_rss(url))

pretty_print(titles)
