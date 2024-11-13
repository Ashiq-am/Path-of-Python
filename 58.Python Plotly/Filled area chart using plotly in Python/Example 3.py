import plotly.express as px


df = px.data.tips()

fig = px.area(df, x ='total_bill', y = 'day')
fig.show()
