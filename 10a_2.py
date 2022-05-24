import nltk
tokens = nltk.word_tokenize(
    "Can we get information on admission for the academic year 2022")
print("Parts of speech:", nltk.pos_tag(tokens))
