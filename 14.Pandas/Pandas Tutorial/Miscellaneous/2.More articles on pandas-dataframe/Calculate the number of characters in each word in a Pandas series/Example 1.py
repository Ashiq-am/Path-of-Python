# Import pandas library
import pandas as pd

# Input series of words
words = pd.Series(['Java', 'Kotlin',
				'Python', 'Scala',
					'Ruby'])
print("Given Series:")
print(words)

# Substituting values using map
rst = words.map(lambda calc: len(calc))
print("No. of characters in each word in the given series:")
print(rst)
