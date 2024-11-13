# import TextBlob
from textblob import TextBlob

gfg = TextBlob("GFG is a good company and always value their employees.")

# using TextBlob.sentiment method
gfg = gfg.sentiment

print(gfg)
