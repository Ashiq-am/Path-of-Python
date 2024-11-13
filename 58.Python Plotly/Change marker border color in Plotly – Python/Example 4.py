# importing library
import plotly.express as px

# importing iris dataset from plotly
df = px.data.iris()

# plotting the scatter_3d plot by
# giving three axis on petal_length,
# petal_width and sepal_length
# and giving color with respect to species
fig = px.scatter_3d(df,x='petal_length',
					y='petal_width',
					z='sepal_length',
					color='species')

# setting up marker and in line Attribute
# giving the width and color of border
fig.update_traces(marker=dict(size=10,
							line=dict(width=10,
										color='red')))

# showing the plot
fig.show()
