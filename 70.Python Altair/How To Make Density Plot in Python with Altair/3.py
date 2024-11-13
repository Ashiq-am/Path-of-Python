# loading a single column into
# the data frame object
d = d[["charges"]]

a.Chart(d).transform_density('charges', as_=['CHARGES', 'DENSITY'],
							).mark_area(color='green').encode(
	x="CHARGES:Q",
	y='DENSITY:Q',

)
