# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 18:18:29 2022

@author: Aayush Shah
"""

import nltk
groucho_grammar = nltk.CFG.fromstring(""" 
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I' 
VP -> V NP | VP PP
Det -> 'a' | 'my'
N -> 'cake' | 'birthday' 
V -> 'baked'
P -> 'on'
""")
sent = ['I', 'baked', 'a', 'cake', 'on', 'my', 'birthday'] 
parser = nltk.ChartParser(groucho_grammar) 
for tree in parser.parse(sent):
    print(tree)
