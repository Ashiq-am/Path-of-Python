import plotly.express as px

# using the wind dataset
df = px.data.wind()

fig = px.bar_polar(df, r="strength", theta="direction",
				color="frequency",)
fig.show()
