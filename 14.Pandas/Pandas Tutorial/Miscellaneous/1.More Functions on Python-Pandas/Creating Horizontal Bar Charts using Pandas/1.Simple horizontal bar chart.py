# Import required libraries
import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({'Cuisine': ['Italian', 'Indian', 'Mexican', 'Chinese'],
				'Number of People': [20, 25, 15, 10]})

# Plot a bar chart
df.plot.barh(x='Cuisine', y='Number of People',
			title='Cuisine Preference', color='green')
