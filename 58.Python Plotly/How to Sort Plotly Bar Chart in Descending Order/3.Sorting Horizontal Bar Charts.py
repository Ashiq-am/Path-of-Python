import plotly.express as px
import pandas as pd

data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [4, 1, 3, 2]
}

df = pd.DataFrame(data)

# Create a horizontal bar chart
fig = px.bar(df, x='Values', y='Category', orientation='h')

# Update layout to sort bars in descending order
fig.update_layout(yaxis={'categoryorder': 'total ascending'})
fig.show()
