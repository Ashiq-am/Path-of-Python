import plotly.express as px

df = px.data.tips()

fig = px.box(df, x = "sex", y="total_bill", points="all")
fig.update_traces(quartilemethod="inclusive")

fig.show()
