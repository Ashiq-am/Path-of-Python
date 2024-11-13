import plotly.express as px

# Create an animated scatter plot with additional features
fig = px.scatter(
    df,
    x='date',
    y='sales',
    animation_frame='date',
    color='category',
    size='profit',  # Use profit for marker size
    title='Monthly Sales and Profit Data (Animated Scatter Plot)',
    labels={'sales': 'Sales Amount', 'date': 'Date'},
    range_y=[0, 1000],
    range_x=[df['date'].min(), df['date'].max()],  # Ensure x-axis covers the full date range
    hover_name='category',  # Show category on hover
    hover_data={'profit': True, 'sales': True},  # Include profit in hover data
    template='plotly_white'  # Change the template for a different aesthetic
)

# Customize layout for better aesthetics
fig.update_layout(
    title_x=0.5,  # Center the title
    xaxis_title='Date',
    yaxis_title='Sales Amount',
    legend_title='Product Category',
    hovermode='closest',
    showlegend=True
)

# Add annotations for significant points if needed
annotations = [
    dict(x='2022-06-01', y=600, text='Mid Year Peak', showarrow=True, arrowhead=2, ax=0, ay=-40),
    dict(x='2023-12-01', y=800, text='End of Year Surge', showarrow=True, arrowhead=2, ax=0, ay=-40)
]

fig.update_layout(annotations=annotations)

# Show the plot
fig.show()
