import altair as alt
import pandas as pd
# Sample data
data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D'],
    'value': [4, 3, 7, 5]
})

# Create a bar chart
bar_chart = alt.Chart(data).mark_bar().encode(
    x='category:O',  # Ordinal data for x-axis
    y='value:Q'      # Quantitative data for y-axis
)

bar_chart
