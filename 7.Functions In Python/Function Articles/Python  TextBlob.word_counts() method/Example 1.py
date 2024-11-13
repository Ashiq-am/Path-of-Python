# import TextBlob
from textblob import TextBlob

gfg = TextBlob("I am confused sometime, sometime I messed up things.")

# using TextBlob.word_counts() method
gfg = gfg.word_counts['sometime']

print(gfg)
