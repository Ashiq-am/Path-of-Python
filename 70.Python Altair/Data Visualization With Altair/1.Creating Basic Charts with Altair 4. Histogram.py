import altair as alt
import pandas as pd

# Sample data
data = pd.DataFrame({
    'Value': [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5]
})

# Create a histogram
histogram = alt.Chart(data).mark_bar().encode(
    alt.X('Value:O', bin=True),
    y='count()'
).properties(
    title='Histogram'
)

histogram.display()
