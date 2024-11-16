# import packages
import pandas as pd
from stop_words import get_stop_words
import re

# stop words
stop_words = get_stop_words('en')

# reading the csv file
data = pd.read_csv('test.csv')

print('Before string processing : ')
print(data[(data['PhraseId'] >= 157139) & (
	data['PhraseId'] <= 157141)]['Phrase'])

# converting all text to lower case in the Phrase column
data['Phrase'] = data['Phrase'].apply(str.lower)

# using regex to remove punctuation
data['Phrase'] = data['Phrase'].apply(lambda x: re.sub(r'[^\w\s]', '', x)
									)

# removing stop words
data['Phrase'] = data['Phrase'].apply(lambda x: ' '.join(
	w for w in x.split() if w not in stop_words))

print('After string processing : ')
data[(data['PhraseId'] >= 157139) & (data['PhraseId'] <= 157141)]['Phrase']
