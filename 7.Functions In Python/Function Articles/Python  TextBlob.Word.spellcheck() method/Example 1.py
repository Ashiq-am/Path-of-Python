# import Word
from textblob import Word

gfg = Word("Facility")

# using Word.spellcheck() method
print(gfg.spellcheck())
