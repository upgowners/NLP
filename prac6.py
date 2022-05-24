# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 17:54:57 2022

@author: hp
"""
import nltk

text = """Founded in 2002, SpaceX‟s mission is to enable humans to become a spacefaring civilization and a multi-planet
species by building a self-sustaining city on Mars. In 2008, SpaceX‟s Falcon 1 became the first privately developed
liquid-fuel launch vehicle to orbit the Earth."""

from nltk import pos_tag
from nltk import RegexpParser

text =text.split() 
print("After Split:",text)

tokens_tag = pos_tag(text)
print("\nAfter Token:",tokens_tag)

patterns= """mychunk:{<NN.?>*<VBD>*<JJ.?>*<CC>?}""" 
chunker = RegexpParser(patterns)
print("\nAfter Regex:",chunker) 
output = chunker.parse(tokens_tag)
print("\nAfter Chunking",output)
