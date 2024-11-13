# Define custom color sequence
custom_colors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA']

# Create a scatter plot with custom colors
fig = px.scatter(
    df,
    x='sepal_width',
    y='sepal_length',
    color='species',
    color_discrete_sequence=custom_colors,
    title='Scatter Plot with Custom Color Sequence'
)

fig.show()
