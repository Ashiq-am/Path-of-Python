import plotly.express as px

df = px.data.tips()

fig = px.scatter(df, x="total_bill", y="tip",
				animation_frame="day",
				color="sex",)

fig["layout"].pop("updatemenus")
fig.show()
