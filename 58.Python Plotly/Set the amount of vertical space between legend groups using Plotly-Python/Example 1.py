# importing packages
import plotly.express as px

# using medals_wide dataset
wide_df = px.data.medals_wide()

# plotting the bar chart
fig = px.bar(wide_df, x="nation", y=[
			"gold", "silver", "bronze"],
			title="Geeksforgeeks")

# spacing legend in plotly in pixels.
fig.update_layout(legend_tracegroupgap=2)

# showing fig.
fig.show()
