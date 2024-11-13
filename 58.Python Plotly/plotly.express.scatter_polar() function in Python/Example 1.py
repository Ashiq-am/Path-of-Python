import plotly.express as px

df = px.data.tips()

plot = px.scatter_polar(df, r = 'day',
						theta = 'total_bill')
plot.show()
