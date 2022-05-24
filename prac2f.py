# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 00:08:24 2022

@author: hp
"""

import nltk
text = nltk.word_tokenize(
    "The night is cold, with a lot of stars in the sky and huge tress alongsides of the road")
tokenized = nltk.pos_tag(text)
print(tokenized)
