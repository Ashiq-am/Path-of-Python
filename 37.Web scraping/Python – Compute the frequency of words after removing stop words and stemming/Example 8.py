from textblob import TextBlob
final_words_sentence=[]
final_words_paragraph=[]
final_words_webpage=[]

for i in range(len(sentence_after_stemming)):
	final_words_sentence.append(0)
	present_word=sentence_after_stemming[i]
	b=TextBlob(sentence_after_stemming[i])
	if str(b.correct()).lower() in nltk_stop_words:
		final_words_sentence[i]=present_word
	else:
		final_words_sentence[i]=str(b.correct())
print(final_words_sentence)
print('\n')

for i in range(len(paragraph_after_stemming)):
	final_words_paragraph.append(0)
	present_word = paragraph_after_stemming[i]
	b = TextBlob(paragraph_after_stemming[i])
	if str(b.correct()).lower() in nltk_stop_words:
		final_words_paragraph[i] = present_word
	else:
		final_words_paragraph[i] = str(b.correct())

print(final_words_paragraph)
print('\n')

for i in range(len(webpage_after_stemming)):
	final_words_webpage.append(0)
	present_word = webpage_after_stemming[i]
	b = TextBlob(webpage_after_stemming[i])
	if str(b.correct()).lower() in nltk_stop_words:
		final_words_webpage[i] = present_word
	else:
		final_words_webpage[i] = str(b.correct())
print(final_words_webpage)
print('\n')
