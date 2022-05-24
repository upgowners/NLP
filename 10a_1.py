import spacy
sp = spacy.load('en_core_web_sm')
sen = sp(u"The Natural Language Processing Practical is performed by Ankit")
print(sen.text)
print(sen[7].pos_)
print(sen[7].tag_)
print(spacy.explain(sen[7].tag_))
for word in sen:
    print(f'{word.text:{12}}{word.pos_:{10}}{word.tag_:{8}}{spacy.explain(word.tag_)}')
