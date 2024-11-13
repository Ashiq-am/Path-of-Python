import plotly.express as px

df = px.data.iris()

# Create a scatter plot
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="Iris Dataset")

# Add annotation
fig.add_annotation(
    x=3.5, y=7.5,
    text="Sample Annotation",
    showarrow=True,
    arrowhead=1
)

fig.show()
