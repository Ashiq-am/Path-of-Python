import plotly.express as px
import pandas as pd

data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [4, 1, 3, 2]
}
df = pd.DataFrame(data)
fig = px.bar(df, x='Category', y='Values')

# Update layout to sort bars in descending order
fig.update_layout(xaxis={'categoryorder': 'total descending'})
fig.show()
