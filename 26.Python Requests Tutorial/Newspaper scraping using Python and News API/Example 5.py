title_combined = ''

for i in response_json['articles']:
    title_combined += i['title'] + ' '

titles = title_combined.replace('\s+',
                                ' ').replace(',',
                                             ' ').replace('.',
                                                          ' ')
words_t = titles.split()
result = [word for word in words_t if
          (word.lower() not in bad_words and
           len(word) > 3)]

result = ' '.join(result)

wordcount = {}

for word in result.split():

    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

word = WordCloud(max_font_size=40).generate(result)
plt.figure()
plt.imshow(word, interpolation="bilinear")
plt.axis("off")
plt.show()
