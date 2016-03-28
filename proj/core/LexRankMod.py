
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import math

try:
    import numpy
except ImportError:
    numpy = None

from sumy.summarizers._summarizer import AbstractSummarizer
from sumy._compat import Counter



class LexRankModSummarizer(AbstractSummarizer):
    threshold = 0.1
    epsilon = 0.1
    _stop_words = frozenset()

    @property
    def stop_words(self):
        return self._stop_words
    
    @stop_words.setter
    def stop_words(self,words):
        self._stop_words = frozenset(map(self.normalize_word, words))
    
    #Overwritten call method to take a query
    def __call__(self, document, sentences_count, query):
        pass
    
    
    
    

