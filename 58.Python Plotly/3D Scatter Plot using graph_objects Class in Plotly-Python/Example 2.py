import plotly.express as px
import plotly.graph_objects as go

df = px.data.iris()

fig = go.Figure(data =[go.Scatter3d(x = df['sepal_width'],
								y = df['sepal_length'],
								z = df['petal_length'],
								mode ='markers')])
fig.show()
