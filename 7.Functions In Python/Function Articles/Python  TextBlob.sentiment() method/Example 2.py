# import TextBlob
from textblob import TextBlob

gfg = TextBlob("Sandeep Jain An IIT Roorkee alumnus and founder of GeeksforGeeks. He loves to solve programming problems in most efficient ways.")

# using TextBlob.sentiment method
gfg = gfg.sentiment

print(gfg)
