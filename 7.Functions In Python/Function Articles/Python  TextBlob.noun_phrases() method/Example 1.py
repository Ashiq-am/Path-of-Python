# import TextBlob
from textblob import TextBlob

gfg = TextBlob("Python is a high-level language.")

# using TextBlob.noun_phrases method
gfg = gfg.noun_phrases

print(gfg)
