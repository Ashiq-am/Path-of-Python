# importing package
import matplotlib.pyplot as plt
import pandas as pd

# create data
df = pd.DataFrame([['A', 10, 20, 10, 30], ['B', 20, 25, 15, 25], ['C', 12, 15, 19, 6],
				['D', 10, 29, 13, 19]],
				columns=['Team', 'Round 1', 'Round 2', 'Round 3', 'Round 4'])
# view data
print(df)

# plot grouped bar chart
df.plot(x='Team',
		kind='bar',
		stacked=False,
		title='Grouped Bar Graph with dataframe')
