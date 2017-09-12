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


from abc import ABC, abstractmethod

import feedparser

from apiMedia.utils import pretty_print


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

class ExpressParser(BaseRSSParser):
    """Express feed parser.
    """
    url = 'http://www.lexpress.fr/rss/alaune.xml'

class LeParisienParser(BaseRSSParser):
    """Le Parisien feed parser.
    """
    url = 'http://www.leparisien.fr/une/rss.xml#xtor=RSS-1481423633'

class RadioCanadaParser(BaseRSSParser):
    """Radio canada feed parser.
    """
    url = 'http://rss.radio-canada.ca/fils/nouvelles/nouvelles.xml'
