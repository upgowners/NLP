# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 17:46:22 2022

@author: hp
"""

from inltk.inltk import get_similar_sentences
from inltk.inltk import setup
setup('hi')
# get similar sentences to the one given in hindi
output = get_similar_sentences('मैं आज बहुि खुश हूं', 5, 'hi')
print('asdasd {output}')
