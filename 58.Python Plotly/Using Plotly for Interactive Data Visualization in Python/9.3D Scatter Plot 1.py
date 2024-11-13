import plotly.express as px

# data to be pltted
df = px.data.tips()

# plotting the figure
fig = px.scatter_3d(df, x="total_bill", y="sex", z="tip", color='day',
					size='total_bill', symbol='time')

fig.show()
