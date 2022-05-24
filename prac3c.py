# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 15:36:22 2022

@author: hp
"""

from nltk.corpus import wordnet 
synonyms = []
antonyms = []
for syn in wordnet.synsets("active"): 
    for l in syn.lemmas():
        synonyms.append(l.name()) 
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print("\nSysnet Synonyms : ",set(synonyms)) 
print("\nSysnet Antonyms : ",set(antonyms))
