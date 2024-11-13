# importing packages
import plotly.express as px

# using the gapminder dataset
df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", color="sex",
				symbol="smoker", facet_col="time",
				labels={"sex": "Gender", "smoker": "Smokes"})

# hiding legend in pyplot express.
fig.update_traces(showlegend=False)

fig.show()
