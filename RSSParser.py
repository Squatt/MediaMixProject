from abc import ABC, abstractmethod

import feedparser

from utils import pretty_print


class BaseRSSParser(ABC):
    """Base class for each RSS feed. This class must no be used as is.
    Parsers for each class should inherit from this class.
    """

    url = ''

    def __init__(self):
        self.raw_content = feedparser.parse(self.url)
        self.entries = self.get_entries()
        self.titles = None

    def get_titles(self):
        """Returns the a list of titles corresponding to the news.
        """
        if self.titles:
            return self.titles

        titles = []
        for entry in self.entries:
            if entry['title'] not in titles:
                titles.append(entry['title'])
        self.titles = titles
        return titles

    def get_entries(self):
        entries = self.raw_content.get('entries')
        return [] if not entries else entries


class LeMondeParser(BaseRSSParser):
    """Le Monde feed parser.
    """

    url = 'http://www.lemonde.fr/rss/une.xml'


class MediaPartParser(BaseRSSParser):
    """MediaPart feed parser.
    """

    url = 'https://www.mediapart.fr/journal/podcast/chronique/rss'
