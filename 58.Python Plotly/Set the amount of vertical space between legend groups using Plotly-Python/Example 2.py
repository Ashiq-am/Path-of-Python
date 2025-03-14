# importing packages
import plotly.express as px

# using the gapminder dataset
df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", color="sex",
				symbol="smoker", facet_col="time",
				labels={"sex": "Gender", "smoker": "Smokes"})

# spaceing between legend in pixel.
fig.update_layout(legend_tracegroupgap=12)

# showing figure.
fig.show()
