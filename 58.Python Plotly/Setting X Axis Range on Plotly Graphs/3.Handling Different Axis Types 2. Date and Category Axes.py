import plotly.graph_objects as go
import pandas as pd

# Generate sample data
dates = pd.date_range(start="2023-01-01", periods=100)
y = np.random.rand(100)

# Create a scatter plot with a date x-axis
fig = go.Figure(go.Scatter(x=dates, y=y))
fig.update_xaxes(range=["2023-01-20", "2023-02-20"])
fig.show()
