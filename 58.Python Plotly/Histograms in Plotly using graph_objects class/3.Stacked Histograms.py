import plotly.express as px
import plotly.graph_objects as go

df = px.data.iris()

fig = go.Figure()
fig.add_trace(go.Histogram(x=df['sepal_width']))
fig.add_trace(go.Histogram(x=df['species_id']))

fig.update_layout(barmode='stack')
fig.show()
