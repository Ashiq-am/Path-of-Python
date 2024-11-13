# import TextBlob
from textblob import TextBlob

gfg = TextBlob("I amm goodd at speling mstake.")

# using TextBlob.correct() method
gfg = gfg.correct()

print(gfg)
