# importing library
import plotly.express as px

# importing iris dataset from plotly
df = px.data.iris()

# plotting the scatter plot on sepal_width
# and sepal_length and giving color with
# respect to species
fig = px.scatter(df, x='sepal_width',
				y='sepal_length',
				color='species')

# showing the plot with default settings
fig.show()
