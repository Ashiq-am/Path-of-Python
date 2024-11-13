import plotly.express as px


df = px.data.tips()

fig = px.bar_polar(df, r="total_bill", theta="time",
				color="sex",)

fig.show()
