# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 15:06:59 2022

@author: Aayush Shah
"""

import nltk
from nltk.corpus import brown
tokens = 'John saw 3 polar bears .'.split() 
default_tagger = nltk.DefaultTagger('NN') 
print(default_tagger.tag(tokens))
brown_tagged_sents = brown.tagged_sents(categories='news') 
print(default_tagger.evaluate(brown_tagged_sents))

patterns = [
(r'.*ing$', 'VBG'),	# gerunds
(r'.*ed$', 'VBD'),	# simple past
(r'.*es$', 'VBZ'),	# 3rd singular present
(r'.*ould$', 'MD'),	# modals
(r'.*\'s$', 'NN$'),	# possessive nouns
(r'.*s$', 'NNS'),	# plural nouns
(r'^-?[0-9]+(\.[0-9]+)?$', 'CD'), # cardinal numbers (r'.*', 'NN')	# nouns (default)
]

regexp_tagger = nltk.RegexpTagger(patterns)
exp=(regexp_tagger.tag("An example of Regular Expression tagger performed by Aayush Shah 17".split()))
print(exp)
brown_tagged_sents = brown.tagged_sents(categories='news') 
print(regexp_tagger.evaluate(brown_tagged_sents)) 
brown_tagged_sents = brown.tagged_sents(categories='news') 
brown_sents = brown.sents(categories='news') 
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents) 
print(unigram_tagger.tag(brown_sents[2007])) 
print(unigram_tagger.evaluate(brown_tagged_sents))
