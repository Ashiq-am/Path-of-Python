# Import pandas library
import pandas as pd

# Input series of words
words = pd.Series(['alphabet', 'consonants',
				'vowels', 'letters'])

# Display length of words
# along with words
for i in range(len(words)):
	print(words[i], words.str.len()[i])
