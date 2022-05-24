# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 15:27:50 2022

@author: Aayush Shah
"""


from nltk.corpus import wordnet
syn = wordnet.synsets('hello')[0]
print ("Synset name : ", syn.name()) 
print ("\nSynset Definition : ", syn.definition())



synonyms = [] 
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name()) 
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print("\nSysnet Synonyms : ",set(synonyms)) 
print("\nSysnet Antonyms : ",set(antonyms))
