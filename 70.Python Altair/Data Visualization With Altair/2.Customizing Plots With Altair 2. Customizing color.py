import altair as alt
import pandas as pd

# Sample data
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [4, 7, 1, 5],
    'Type': ['X', 'Y', 'X', 'Y']
})

# Create a bar plot with a color scale
bar_chart = alt.Chart(data).mark_bar().encode(
    x='Category',
    y='Value',
    color=alt.Color('Type:N', scale=alt.Scale(domain=['X', 'Y'], range=['#1f77b4', '#ff7f0e']))
).properties(
    title='Bar Plot with Color Scale'
)

bar_chart
