import altair as alt
import pandas as pd

# Sample Data
data = pd.DataFrame({
    'x': ['A', 'B', 'C', 'D'],
    'y': [5, 10, 15, 20]
})

# Create the chart
chart = alt.Chart(data).mark_bar().encode(
    x='x',
    y='y'
).configure(
    background='lightgray'  # Setting the background color
)


# Display the chart
chart
