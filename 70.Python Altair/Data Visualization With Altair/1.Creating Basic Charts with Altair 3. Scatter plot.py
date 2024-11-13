import altair as alt
import pandas as pd

# Sample data
data = pd.DataFrame({
    'X': [1, 2, 3, 4, 5],
    'Y': [10, 15, 13, 17, 19]
})

# Create a scatter plot
scatter_plot = alt.Chart(data).mark_point().encode(
    x='X',
    y='Y'
).properties(
    title='Scatter Plot'
)

scatter_plot.display()
