# Removing Punctuation
def remove_punct(text):
	text = "".join([char for char in text if
					char not in string.punctuation])
	text = re.sub('[0-9]+', '', text)
	return text


tw_list['punct'] = tw_list['content'].apply(
lambda x: remove_punct(x))

# Appliyng tokenization
def tokenization(text):
	text = re.split('\W+', text)
	return text


tw_list['tokenized'] = tw_list['punct'].apply(
	lambda x: tokenization(x.lower()))

# Removing stopwords
stopword = nltk.corpus.stopwords.words('english')

def remove_stopwords(text):
	text = [word for word in text if
			word not in stopword]
	return text

tw_list['nonstop'] = tw_list['tokenized'].apply(
lambda x: remove_stopwords(x))

# Appliyng Stemmer
ps = nltk.PorterStemmer()

def stemming(text):
	text = [ps.stem(word) for word in text]
	return text

tw_list['stemmed'] = tw_list['nonstop'].apply(
lambda x: stemming(x))

tw_list.head()
