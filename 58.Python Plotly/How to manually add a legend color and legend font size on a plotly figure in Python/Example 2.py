# importing packages
import plotly.express as px

# using the gapminder dataset
df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", color="sex",
				symbol="smoker", facet_col="time",
				labels={"sex": "Gender", "smoker": "Smokes"})

# set legend color
fig.update_layout(legend_font_color="gold")

# set font size
fig.update_layout(legend_font_size=10)

fig.show()
