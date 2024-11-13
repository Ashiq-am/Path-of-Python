import plotly.graph_objects as go
from datetime import datetime

# Sample data with empty dates
dates = [
    datetime(2023, 6, 1),
    datetime(2023, 6, 3),
    datetime(2023, 6, 5),
    datetime(2023, 6, 7),
    datetime(2023, 6, 9),
    # datetime(2023, 6, 11),
    datetime(2023, 6, 13)
]
values = [10, 15, 7, 20, 12, 18]

# Create a figure
fig = go.Figure()

# Add trace with missing date
fig.add_trace(go.Scatter(x=dates, y=values, mode='lines+markers'))

# Update layout to remove empty dates
fig.update_xaxes(type='category', rangebreaks=[dict(values=['2023-06-13'])])

# Show the plot
fig.show()
