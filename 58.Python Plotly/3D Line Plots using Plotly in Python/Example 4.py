import plotly.express as px


df = px.data.tips()

fig = px.line_3d(df, x="total_bill", y="day", z="time")
fig.show()
