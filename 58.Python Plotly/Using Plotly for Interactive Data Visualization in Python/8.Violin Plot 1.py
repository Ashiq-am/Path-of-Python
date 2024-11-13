import plotly.express as px

# using the dataset
df = px.data.tips()

# plotting the violin plot
fig = px.violin(df, x="day", y="tip", color='sex',
				facet_row='time', box=True)

# showing the plot
fig.show()
