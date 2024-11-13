# imports
import plotly.express as px

# using elections dataset
df = px.data.election()

# figure setup
fig = px.scatter_ternary(df, a="Joly", b="Coderre", c="Bergeron", hover_name="district",
	color="total", size="total", size_max=15, symbol ='Coderre',
	color_discrete_map = {"Joly": "blue", "Bergeron": "green", "Coderre":"red"}, title="Geeksforgeeks"
	)

# move colorbar
fig.update_layout(coloraxis_colorbar=dict(yanchor="top", y=1, x=0,
										ticks="outside",
										ticksuffix=" bills"))
# hiding legend
fig.update(layout_showlegend=False)

# hiding color-bar
fig.update(layout_coloraxis_showscale=False)

fig.show()
