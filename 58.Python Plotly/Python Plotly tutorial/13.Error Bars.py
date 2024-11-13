import plotly.express as px

# using the iris dataset
df = px.data.iris()

# Calculating the error field
df["error"] = df["petal_length"]/100

# plotting the scatter chart
fig = px.scatter(df, x="species", y="petal_width",
				error_x="error", error_y="error")

# showing the plot
fig.show()

