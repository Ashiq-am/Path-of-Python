# import libraries
import altair as alt
import pandas as pd
import numpy as np
np.random.seed(1)

# create data
df = pd.DataFrame({'X':np.random.randint(1, 10, 50),
				'Y':np.random.randint(1, 10, 50),
				'Cluster':np.random.randint(1, 5, 50)})

# Draw Facet Scatter Plot
alt.Chart(df).mark_point().encode(
	x=alt.X('X'),
	y=alt.Y('Y')
).properties(width = 200, height = 200).facet(
	'Cluster:N',
	columns = 2
)
