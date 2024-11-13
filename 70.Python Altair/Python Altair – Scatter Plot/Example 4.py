# depict scatter plot
alt.Chart(seattle_weather).mark_point().encode(
	x='temp_max',
	y='temp_min'
)
