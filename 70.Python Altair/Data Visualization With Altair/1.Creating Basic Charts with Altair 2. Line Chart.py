import altair as alt
import pandas as pd

# Sample data
data = pd.DataFrame({
    'Year': [2000, 2001, 2002, 2003, 2004],
    'Value': [10, 15, 8, 12, 18]
})

# Create a line plot
line_chart = alt.Chart(data).mark_line().encode(
    x='Year',
    y='Value'
).properties(
    title='Line Plot'
)

line_chart.display()
