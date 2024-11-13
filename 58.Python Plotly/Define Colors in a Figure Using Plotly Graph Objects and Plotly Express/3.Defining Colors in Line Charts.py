# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 8, 13]

# Define colors
line_color = 'blue'
marker_color = 'red'

# Create a line chart
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x, y=y,
    mode='lines+markers',
    line=dict(color=line_color),
    marker=dict(color=marker_color, size=10),
    name='Fibonacci'
))

fig.update_layout(title='Line Chart with Custom Colors')
fig.show()
