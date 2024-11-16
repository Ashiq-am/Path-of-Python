# import pandas library as pd
import pandas as pd

# create an Empty DataFrame object
df = pd.DataFrame()

print(df)

# append columns to an empty DataFrame
df['Name'] = ['Ankit', 'Ankita', 'Yashvardhan']
df['Articles'] = [97, 600, 200]
df['Improved'] = [2200, 75, 100]

df
