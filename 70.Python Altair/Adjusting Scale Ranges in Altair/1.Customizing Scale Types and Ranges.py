import altair as alt
import pandas as pd

# Sample data with a wide range
data = pd.DataFrame({
    'x': [1, 10, 100, 1000, 10000],
    'y': [2, 20, 200, 2000, 20000]
})

# Create a scatter plot with a logarithmic scale
chart = alt.Chart(data).mark_circle(size=60).encode(
    x=alt.X('x', scale=alt.Scale(type='log', domain=[1, 10000])),  # Log scale on x-axis
    y=alt.Y('y', scale=alt.Scale(type='log', domain=[1, 20000]))   # Log scale on y-axis
)

chart.show()
