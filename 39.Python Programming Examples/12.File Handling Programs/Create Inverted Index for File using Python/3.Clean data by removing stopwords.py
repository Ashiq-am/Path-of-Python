from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

for i in range(1):
	# this will convert
	# the word into tokens
	text_tokens = word_tokenize(read)

tokens_without_sw = [
	word for word in text_tokens if not word in stopwords.words()]

print(tokens_without_sw)
