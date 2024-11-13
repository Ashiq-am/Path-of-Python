# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 30, 40, 50]

# Define colors
colors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A']

# Create a bar chart
fig = go.Figure()

fig.add_trace(go.Bar(
    x=categories,
    y=values,
    marker=dict(color=colors),
    name='Values'
))

fig.update_layout(title='Bar Chart with Custom Colors')
fig.show()
