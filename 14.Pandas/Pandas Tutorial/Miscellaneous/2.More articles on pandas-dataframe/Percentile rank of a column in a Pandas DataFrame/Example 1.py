# import the module
import pandas as pd

# create a DataFrame
data = {'Name': ['Mukul', 'Rohan', 'Mayank',
				'Shubham', 'Aakash'],
		'Location' : ['Saharanpur', 'Meerut', 'Agra',
					'Saharanpur', 'Meerut'],
		'Pay' : [50000, 70000, 62000, 67000, 56000]}
df = pd.DataFrame(data)

# create a new column of percentile rank
df['Percentile Rank'] = df.Pay.rank(pct = True)

# displaying the percentile rank
display(df)
