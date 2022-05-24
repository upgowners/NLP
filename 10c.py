from nltk.parse import malt
mp = malt.MaltParser('C://Users//ankit//Desktop//MSCIT//NLP//Code//.venv//Scripts//maltparser-1.9.2',
                     'C://Users//ankit//Desktop//MSCIT//NLP//Code//.venv//Scripts//engmalt.linear-1.7.mco')  # file
t = mp.parse_one('The nlp practical is performed by Ankit.'.split()).tree()
print(t)
t.draw()
