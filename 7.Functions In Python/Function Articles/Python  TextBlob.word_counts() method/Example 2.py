# import TextBlob
from textblob import TextBlob

gfg = TextBlob("My name is Khan khan KhaN.")

# using TextBlob.word_counts() method
gfg = gfg.word_counts['khan']

print(gfg)
