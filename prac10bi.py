# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 19:09:18 2022

@author: hp
"""


import nltk
tokens=nltk.word_tokenize("Can we get information on admission for the academic year 2021") 
print("Parts of speech:",nltk.pos_tag(tokens))
