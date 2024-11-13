# initializing bad_chars_list
bad_words = ["a", "the", "of", "in", "to", "and", "on", "de", "with",
             "by", "at", "dans", "ont", "été", "les", "des", "au", "et",
             "après", "avec", "qui", "par", "leurs", "ils", "a", "pour",
             "les", "on", "as", "france", "eux", "où", "son", "le", "la",
             "en", "with", "is", "has", "for", "that", "an", "but", "be",
             "are", "du", "it", "à", "had", "ist", "Der", "um", "zu", "den",
             "der", "-", "und", "für", "Die", "von", "als",
             "sich", "nicht", "nach", "auch"]

r = text_combined.replace('\s+',
                          ' ').replace(',',
                                       ' ').replace('.',
                                                    ' ')
words = r.split()
rst = [word for word in words if
       (word.lower() not in bad_words
        and len(word) > 3)]

rst = ' '.join(rst)

wordcount = {}

for word in rst.split():

    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for k, v, in sorted(wordcount.items(),
                    key=lambda words: words[1],
                    reverse=True):
    print(k, v)
