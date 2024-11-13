import plotly.express as px

df = px.data.tips()

fig = px.bar(df, x="tota_bill", y="day",
			color="sex", barmode = 'group')

fig.show()
