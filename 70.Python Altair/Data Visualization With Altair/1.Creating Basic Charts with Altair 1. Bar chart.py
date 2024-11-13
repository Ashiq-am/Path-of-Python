import altair as alt
import pandas as pd

# Sample data
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [4, 7, 1, 5]
})

# Create a bar plot
bar_chart = alt.Chart(data).mark_bar().encode(
    x='Category',
    y='Value'
).properties(
    title='Bar Plot'
)

bar_chart.display()
