# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 18:14:44 2022

@author: Ankit Patel
"""

import nltk

cp = nltk.RegexpParser('CHUNK: {<V.*> <TO> <V.*>}')
treebank = nltk.corpus.treebank
for sent in treebank.tagged_sents():
    tree = cp.parse(sent)
    for subtree in tree.subtrees():
        if subtree.label() == 'CHUNK':
            print(subtree)
