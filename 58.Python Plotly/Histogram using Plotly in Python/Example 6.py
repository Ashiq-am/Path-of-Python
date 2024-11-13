import plotly.express as px

df = px.data.tips()

fig = px.histogram(df, x="total_bill", marginal = 'box')
fig.show()
