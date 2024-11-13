px.choropleth(dataset2,
			locations='iso_alpha',
			color="Recovered",
			hover_name="Country/Region",
			color_continuous_scale="RdYlGn",
			projection="natural earth",
			animation_frame="Date" )
