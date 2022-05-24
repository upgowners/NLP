# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 18:48:38 2022

@author: hp
"""

from nltk.stem import PorterStemmer 
from nltk.stem import LancasterStemmer 
from nltk.stem import RegexpStemmer
from nltk.stem.snowball import SnowballStemmer 
from nltk.tokenize import word_tokenize
ps = PorterStemmer()
ls = LancasterStemmer()
rs = RegexpStemmer('ing$|s$|e$|able$', min=4) 

ss = SnowballStemmer(language='english')
# choose some words to be stemmed
sentence = "Reading is enjoying a world of fantasy" 
words = word_tokenize(sentence)

for w in words:
    print("\n",w, "<== Porter Stemmer ==>: ", ps.stem(w)) 
    print(w, "<== Lancaster Stemmer ==>: ", ls.stem(w))
    print(w, "<== RegEx Stemmer ==>: ", rs.stem(w)) 
    print(w, "<== Snowball Stemmer ==>: ", ss.stem(w))
