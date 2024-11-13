# import TextBlob
from textblob import TextBlob

gfg = TextBlob("GFG is a good compny and alays valule ttheir employes.")

# using TextBlob.correct() method
gfg = gfg.correct()

print(gfg)
