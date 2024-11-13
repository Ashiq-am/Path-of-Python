import plotly.express as px


df = px.data.tips()
fig = px.parallel_coordinates(
	df, dimensions=['tip', 'total_bill', 'day','time'],)

fig.show()
