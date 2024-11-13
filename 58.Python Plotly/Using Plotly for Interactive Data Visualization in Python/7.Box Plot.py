import plotly.express as px

# using the dataset
df = px.data.tips()

# plotting the boxplot
fig = px.box(df, x="day", y="tip")

# showing the plot
fig.show()
