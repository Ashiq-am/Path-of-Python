# import graph_objects from plotly package
import plotly.graph_objects as go

# import make_subplots function from plotly.subplots
# to make grid of plots
from plotly.subplots import make_subplots

# use specs parameter in make_subplots function
# to create secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# plot a bar chart by specifying the x and y values
# Use add_trace function to specify secondary_y axes.
fig.add_trace(
	go.Bar(x=[10, 20, 30], y=[40, 50, 60], name="yaxis values"),
	secondary_y=False)

# Use add_trace function and specify secondary_y axes = True.
fig.add_trace(
	go.Bar(x=[20, 30, 40], y=[400, 500, 600], name="yaxis2 values"),
	secondary_y=True,)

# Adding title text to the figure
fig.update_layout(
	title_text="Multiple Y Axis in Plotly"
)

# Naming x-axis
fig.update_xaxes(title_text="X - axis")

# Naming y-axes
fig.update_yaxes(title_text="<b>Main</b> Y - axis ", secondary_y=False)
fig.update_yaxes(title_text="<b>secondary</b> Y - axis ", secondary_y=True)
