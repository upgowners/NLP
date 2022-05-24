# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 19:08:36 2022

@author: hp
"""

import spacy
sp = spacy.load('en_core_web_sm')
sen = sp(u"I like to play football. I hated it in my childhood though") 
print(sen.text)
print(sen[7].pos_) 
print(sen[7].tag_) 
print(spacy.explain(sen[7].tag_)) 
for word in sen:
    print(f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}')
