# import the module
import pandas as pd

# create a DataFrame
ODI_runs = {'name': ['Tendulkar', 'Sangakkara', 'Ponting',
					'Jayasurya', 'Jayawardene', 'Kohli',
					'Haq', 'Kallis', 'Ganguly', 'Dravid'],
			'runs': [18426, 14234, 13704, 13430, 12650,
					11867, 11739, 11579, 11363, 10889]}
df = pd.DataFrame(ODI_runs)

# create a new column of percentile rank
df['Percentile Rank'] = df.runs.rank(pct = True)

# displaying the percentile rank
display(df)
