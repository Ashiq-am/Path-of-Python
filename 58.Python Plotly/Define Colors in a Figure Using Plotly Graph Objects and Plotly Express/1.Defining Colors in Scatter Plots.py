import plotly.graph_objects as go

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 11, 12, 13, 14]

# Define colors
colors = ['red', 'green', 'blue', 'orange', 'purple']

# Create a scatter plot
fig = go.Figure()

for i in range(len(x)):
    fig.add_trace(go.Scatter(
        x=[x[i]], y=[y[i]],
        mode='markers',
        marker=dict(color=colors[i], size=15),
        name=f'Point {i+1}'
    ))

fig.update_layout(title='Scatter Plot with Custom Colors')
fig.show()
