# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 15:40:26 2022

@author: Aayush Shah
"""


from nltk.corpus import wordnet 
print("\nComparing ship and boat:") 
n1 = wordnet.synset('ship.n.01')
n2 = wordnet.synset('boat.n.01') 
print(n1.wup_similarity(n2)) 
print("\nComparing bus and boat:")
n1 = wordnet.synset('bus.n.01') 
n2 = wordnet.synset('boat.n.01')
print(n1.wup_similarity(n2))
print("\nComparing red and green:") 
n1 = wordnet.synset('red.n.01')
n2 = wordnet.synset('green.n.01') 
print(n1.wup_similarity(n2))
