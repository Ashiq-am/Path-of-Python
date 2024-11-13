from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
sentence_after_stemming= []
paragraph_after_stemming =[]
webpage_after_stemming = [] #creating empty lists for storing stemmed words
for word in sentence_without_stopwords:
	sentence_after_stemming.append(stemmer.stem(word))
for word in paragraph_without_stopwords:
	paragraph_after_stemming.append(stemmer.stem(word))
for word in webpage_without_stopwords:
	webpage_after_stemming.append(stemmer.stem(word))
