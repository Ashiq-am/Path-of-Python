import altair as alt
import pandas as pd

# Sample data
data = pd.DataFrame({
    'Category': ['A', 'A', 'A', 'B', 'B', 'B'],
    'Value': [1, 2, 3, 4, 5, 6]
})

# Create a box plot
box_plot = alt.Chart(data).mark_boxplot().encode(
    x='Category',
    y='Value'
).properties(
    title='Box Plot'
)

box_plot.display()
