from nltk.corpus import stopwords
nltk.download('stopwords')
nltk_stop_words = stopwords.words('english')
sentence_without_stopwords = [i for i in sentence_after_tokenizing if not i.lower() in nltk_stop_words]
paragraph_without_stopwords = [j for j in paragraph_after_tokenizing if not j.lower() in nltk_stop_words]
webpage_without_stopwords = [k for k in webpage_after_tokenizing if not k.lower() in nltk_stop_words]
