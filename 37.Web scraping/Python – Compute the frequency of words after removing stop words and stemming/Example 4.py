from nltk.tokenize import word_tokenize
import re
sentence_without_punctuations = re.sub(r'[^\w\s]', '', sentence)
paragraph_without_punctuations = re.sub(r'[^\w\s]', '', paragraph)
web_page_paragraphs_without_punctuations = re.sub(r'[^\w\s]', '', web_page_data)
