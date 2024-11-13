# Program to draw scatter plot using Dataframe.plot
# Import libraries
import pandas as pd

# Prepare data
data={'Name':['Dhanashri', 'Smita', 'Rutuja',
			'Sunita', 'Poonam', 'Srushti'],
	'Age':[ 20, 18, 27, 50, 12, 15]}

# Load data into DataFrame
df = pd.DataFrame(data = data)

# Draw a scatter plot and here size of dots determined by age of person
df.plot.scatter(x = 'Name', y = 'Age', s = 'Age', c = 'red')
