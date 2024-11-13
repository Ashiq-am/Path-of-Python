import altair as alt
import pandas as pd

# Sample Data
data = pd.DataFrame({
    'x': ['A', 'B', 'C', 'D'],
    'y': [5, 10, 15, 20]
})

# Create the chart with axis customizations
chart = alt.Chart(data).mark_bar().encode(
    x=alt.X('x', axis=alt.Axis(
        title='Categories',            # Title of the x-axis
        titleFontSize=15,              # Font size for the axis title
        labelFontSize=12,              # Font size for the axis labels
        labelAngle=0,                  # Angle of the axis labels
        labelColor='blue',             # Color of the axis labels
        titleColor='red'               # Color of the axis title
    )),
    y=alt.Y('y', axis=alt.Axis(
        title='Values',
        titleFontSize=15,
        labelFontSize=12,
        grid=True,                     # Show grid lines
        titleAngle=90,                  # Title angle (default is 90 for y-axis)
        titleColor='green'             # Color of the y-axis title
    ))
).properties(
    title='Customized Axes'
)

# Display the chart
chart
