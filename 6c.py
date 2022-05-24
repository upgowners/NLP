from nltk.corpus import treebank_chunk
import nltk
nltk.download('treebank')
treebank_chunk.tagged_sents()[0]
treebank_chunk.chunked_sents()[0]
treebank_chunk.chunked_sents()[0].draw()
