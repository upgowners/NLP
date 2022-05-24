""" # rum from that link
from inltk.inltk import get_similar_sentences
from inltk.inltk import setup
setup('hi')
# get similar sentences to the one given in hindi
output = get_similar_sentences('मैं आज बहुि खुश हूं', 5, 'hi')
print(output)
 """

from inltk.inltk import identify_language
from inltk.inltk import setup
setup('gu')
# Identify the Lnaguage of given text
identify_language('બીના કાપડિયા')
