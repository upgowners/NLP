# rum from that link
from inltk.inltk import tokenize
from inltk.inltk import setup
setup('hi')
hindi_text = """प्राकृ तिक भाषा सीखना बहुि तिलचस्प है।"""
# tokenize(input text, language code)
print(tokenize(hindi_text, "hi"))
