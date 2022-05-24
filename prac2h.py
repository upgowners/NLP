# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 15:24:44 2022

@author: Ankit Patel
"""


def word_count(str):
    counts = dict()
    str = str.lower()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


print(word_count('The Quick Brown fox jumps over the lazy dog.'))
