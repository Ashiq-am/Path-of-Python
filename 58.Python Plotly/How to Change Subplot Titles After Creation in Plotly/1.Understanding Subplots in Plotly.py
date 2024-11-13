import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Create a subplot figure with 1 row and 2 columns
fig = make_subplots(rows=1, cols=2, subplot_titles=("Plot 1", "Plot 2"))

# Add traces to the subplots
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]), row=1, col=1)
fig.add_trace(go.Bar(x=[1, 2, 3], y=[6, 5, 4]), row=1, col=2)

# Display the figure
fig.show()
