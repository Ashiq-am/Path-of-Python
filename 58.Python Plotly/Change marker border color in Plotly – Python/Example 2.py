# importing library
import plotly.express as px

# importing iris dataset from plotly
df = px.data.iris()

# plotting the scatter plot on sepal_width
# and sepal_length and giving color
# with respect to species
fig = px.scatter(df, x='sepal_width',
				y='sepal_length',
				color='species')

# setting up marker and in line
# Attribute giving the width and color of border
fig.update_traces(marker=dict(size=10,
							line=dict(width=3,
										color='blue')))

# showing the plot with default settings
fig.show()
