# import packages
import plotly.express as px
import pandas as pd

# importing csv file
df = pd.read_csv("iris.csv")

# scatter plot using plotly
fig = px.scatter(df, x="sepal_length",
				y="sepal_width",
				color="species")

# adding different style parameters to the legend
fig.update_layout(
	legend=dict(
		x=0,
		y=1,
		title_font_family="Times New Roman",
		font=dict(
			family="Courier",
			size=12,
			color="black"
		),
		bgcolor="LightBlue",
		bordercolor="Black",
		borderwidth=1
	)
)
fig.show()
