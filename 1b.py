from gtts import gTTS
import os
mytext = 'Practical of text to Speech performed by Ankit Patel'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("Ankit1b.wav")
os.system("Ankit1b.wav")
