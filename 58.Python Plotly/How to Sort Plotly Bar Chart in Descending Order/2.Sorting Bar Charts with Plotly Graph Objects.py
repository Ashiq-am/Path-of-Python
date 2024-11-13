import plotly.graph_objects as go

categories = ['A', 'B', 'C', 'D']
values = [4, 1, 3, 2]

fig = go.Figure(go.Bar(x=categories, y=values))

# Update layout to sort bars in descending order
fig.update_layout(xaxis={'categoryorder': 'total descending'})
fig.show()
