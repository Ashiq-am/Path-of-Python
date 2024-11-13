import plotly.express as px
import plotly.graph_objects as go

df = px.data.iris()

fig = go.Figure(data=[go.Histogram(x=df['sepal_width'],
                                   cumulative_enabled=True)])
fig.show()
