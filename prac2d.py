# -*- coding: utf-8 -*-
"""
Created on Tue May 24 16:18:55 2022

@author: hp
"""

from nltk import tokenize
para = "Hello! My name is Ankit Patel. Today you'll be learning NLTK."
sents = tokenize.sent_tokenize(para)
print("\nsentence tokenization\n===================\n", sents)
# word tokenization
print("\nword tokenization\n===================\n")
for index in range(len(sents)):
    words = tokenize.word_tokenize(sents[index])
    print(words)
