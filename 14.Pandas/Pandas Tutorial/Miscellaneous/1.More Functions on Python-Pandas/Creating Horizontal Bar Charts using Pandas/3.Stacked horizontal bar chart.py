# Import required libraries
import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({'Number of Males': [10, 15, 25, 14],
				'Number of Females': [20, 25, 15, 10]},
				index=['Italian', 'Indian', 'Mexican', 'Chinese'])

# Convert numeric values to percentage of whole
percent_df = df.apply(lambda x: (x * 100) / sum(x), axis=1)

# Plot stacked horizontal bar chart
percent_df.plot.barh(stacked=True,
					title="Male-Female percentage composition of Cuisine preferences")
