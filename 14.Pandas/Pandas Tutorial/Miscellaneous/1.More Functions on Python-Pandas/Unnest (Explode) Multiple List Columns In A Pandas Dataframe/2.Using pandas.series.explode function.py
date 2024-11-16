# Import the Pandas library
import pandas as pd

# Create a data frame that has nested columns
df = pd.DataFrame({'Name': ['Arun','Aniket','Ishita', 'Raghav','Vinayak'],
				'Favourite Ice-cream':[['Strawberry', 'Choco-chips'],
										['Vanilla', 'Black Currant'],
										['Butterscotch', 'Chocolate'],
										['Mango', 'Choco-chips'],
										['Kulfi', 'Kaju-Kishmish']],
				'Favourite Soft-Drink':[['Coca Cola', 'Lemonade'],
										['Thumbs Up', 'Sprite'],
										['Moutain Dew', 'Fanta'],
										['Mirinda', 'Maaza'],
										['7Up', 'Sprite']]})

# Print the actual data frame
print ('Actual dataframe:\n',df)

# Unnest the nested columns
df=df.set_index(['Name']).apply(pd.Series.explode).reset_index()

# Print the unnested data frame
print ('\nDataframe after unnesting:\n',df)
