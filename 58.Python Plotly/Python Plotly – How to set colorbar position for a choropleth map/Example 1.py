# importing libraries
import plotly.express as px

# figure setup using dataset
fig = px.choropleth(locations=["CA", "TX", "NY"],
					locationmode="USA-states",
					color=[1, 2, 3], scope="usa",
					title="Geeksforgeeks")

# set colorbar position for X-axis
fig.update_layout(coloraxis_colorbar_x=0.26)

fig.show()
