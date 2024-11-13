from wordcloud import WordCloud
import matplotlib.pyplot as plt

text_combined = ''

for i in response_json['articles']:

    if i['description'] != None:
        text_combined += i['description'] + ' '

wordcount = {}
for word in text_combined.split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for k, v, in sorted(wordcount.items(),
                    key=lambda words: words[1],
                    reverse=True):
    print(k, v)
