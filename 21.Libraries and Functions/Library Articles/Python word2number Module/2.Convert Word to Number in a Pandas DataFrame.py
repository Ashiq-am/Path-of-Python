import pandas as pd
from word2number import w2n

# Create a DataFrame with a column of number words
data = {'Number Words': ['five hundred', 'sixty two', 'three thousand']}
df = pd.DataFrame(data)

# Convert number words to numbers using apply and word_to_num
df['Numerical Values'] = df['Number Words'].apply(w2n.word_to_num)
print(df)
