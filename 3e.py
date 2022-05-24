import spacy
from gensim.parsing.preprocessing import remove_stopwords
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
text = "Ankit Patel likes watching movies. one of his most favourite genre is romance"
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in
                     stopwords.words()]
print(tokens_without_sw)
filtered_sentence = (" ").join(tokens_without_sw)
print("NLTK: ", filtered_sentence)
filtered_sentence = remove_stopwords(text)
print("Genism:", filtered_sentence)
sp = spacy.load('en_core_web_sm')
all_stopwords = sp.Defaults.stop_words
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
filtered_sentence = (" ").join(tokens_without_sw)
print("Spacy: ", filtered_sentence)
