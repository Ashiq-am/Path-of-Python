import plotly.graph_objects as go
from datetime import datetime

# Sample data with empty dates
dates = [
    datetime(2023, 7, 1),
    datetime(2023, 7, 3),
    datetime(2023, 7, 5),
    datetime(2023, 7, 7),
    datetime(2023, 7, 9),
    # Missing date: datetime(2023, 7, 11)
    datetime(2023, 7, 13)
]
values = [25, 30, 15, 22, 18, 27]

# Create a figure
fig = go.Figure()

# Add bar trace with missing date
fig.add_trace(go.Bar(x=dates, y=values))

# Update layout to remove empty dates
fig.update_xaxes(type='category', rangebreaks=[dict(values=['2023-07-13'])])

# Show the plot
fig.show()
