import plotly.graph_objects as go

fig = go.Figure(go.Pie(
	name = "",
	values = [2, 5, 3, 2.5],
	labels = ["R", "Python", "Java Script", "Matlab"],
	text = ["R", "Python", "JS", "Matlab"],
	hovertemplate = "%{label}: <br>Popularity: %{percent} </br> %{text}"
))

fig.show()