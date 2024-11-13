import plotly.express as px


fig = px.treemap(
	names = ["A","B", "C", "D", "E"],
	parents = ["", "A", "B", "C", "A"]
)

fig.show()
