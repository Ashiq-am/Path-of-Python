# import ploty.express libraray
import plotly.express as px

# Load data
df = px.data.election()

# Create choropleth map
fig = px.choropleth(df,
					locations="district",
					color="Bergeron",
					hover_name="district",
					range_color=[0, 50],
					color_continuous_scale="agsunset")

# Resize map by height and width
fig.update_layout(height=400,
				width=600)

# Show map
fig.show()
