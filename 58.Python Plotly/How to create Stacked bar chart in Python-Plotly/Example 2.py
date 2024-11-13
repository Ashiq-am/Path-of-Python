import plotly.express as px

df = px.data.tips()

fig = px.bar(df, x="total_bill", y="day",
			color="sex", barmode = 'stack')

fig.show()
