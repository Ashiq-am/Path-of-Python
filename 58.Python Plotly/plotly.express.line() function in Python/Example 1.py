import plotly.express as px

df = px.data.tips()

plot = px.line(df, x = 'day', y = 'time')
plot.show()
