import pandas as pd
import altair as alt

# Sample data containing zero and negative values
data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 0, -5, 15, 20]  # Zero and negative values included
})

# Create a scatter plot with a logarithmic scale on the y-axis
chart = alt.Chart(data).mark_circle().encode(
    x='x',
    y=alt.Y('y', scale=alt.Scale(type='log'))  # Logarithmic scale on y-axis
)

# Display the chart
chart
