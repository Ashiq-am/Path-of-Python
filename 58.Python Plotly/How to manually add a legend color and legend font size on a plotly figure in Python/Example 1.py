# importing packages
import plotly.express as px

# using medals_wide dataset
wide_df = px.data.medals_wide()

# plotting the bar chart
fig = px.bar(wide_df, x="nation", y=[
			"gold", "silver", "bronze"],
			title="Geeksforgeeks")

# set legend color
fig.update_layout(legend_font_color="red")

# set font size
fig.update_layout(legend_font_size=19)

# showing figure.
fig.show()
