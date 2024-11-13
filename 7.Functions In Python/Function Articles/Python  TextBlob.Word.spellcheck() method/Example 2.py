# import Word
from textblob import Word

gfg = Word("Prediction")

# using Word.spellcheck() method
print(gfg.spellcheck())
