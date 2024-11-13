import altair as alt
import pandas as pd

# Sample data
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [4, 7, 1, 5]
})

# Create a bar plot with custom configurations
bar_chart = alt.Chart(data).mark_bar().encode(
    x='Category',
    y='Value'
).properties(
    title='Bar Plot with Custom Configurations'
).configure(
    title={
        "fontSize": 20,
        "font": "Arial",
        "color": "blue"
    },
    axis={
        "titleFontSize": 14,
        "labelFontSize": 12
    }
)

bar_chart
