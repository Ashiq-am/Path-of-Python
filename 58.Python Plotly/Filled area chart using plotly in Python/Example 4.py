import plotly.express as px


df = px.data.tips()


fig = px.area(df, x ='time', y = 'day',
			color="total_bill")
fig.show()
