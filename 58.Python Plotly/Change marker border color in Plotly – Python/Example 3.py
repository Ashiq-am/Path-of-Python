# importing library
import plotly.express as px

# importing iris dataset from plotly
df = px.data.iris()

# plotting the scatter 3d plot by giving
# three axis, petal length, petal width
# and sepal length
# giving color with respect to species
fig = px.scatter_3d(df,x='petal_length',
					y='petal_width',
					z='sepal_length',
					color='species')

# showing the plot with default settings
fig.show()
