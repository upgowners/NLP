# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 17:41:24 2022

@author: hp
"""

from inltk.inltk import tokenize
from inltk.inltk import setup
setup('hi')
hindi_text = """प्राकृतिक भाषा सीखना बहुि तिलचस्प है।"""
# tokenize(input text, language code)
print(tokenize(hindi_text, "hi"))
