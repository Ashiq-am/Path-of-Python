import plotly.express as px

df = px.data.tips()

fig = px.sunburst(df, path=['day', 'sex'],
				values='total_bill', color='total_bill')
fig.show()
