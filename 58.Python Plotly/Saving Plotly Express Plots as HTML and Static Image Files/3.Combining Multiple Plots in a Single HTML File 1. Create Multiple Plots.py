import plotly.express as px
df = px.data.iris()
fig1 = px.scatter(df, x='sepal_width', y='sepal_length', color='species')
fig2 = px.scatter(df, x='petal_width', y='petal_length', color='species')
