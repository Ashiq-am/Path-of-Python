# importing libraries
import pandas as pd
import altair as alt
import numpy as np


np.random.seed(42)

# creating data
df = pd.DataFrame({'Col A': np.random.normal(-1, 1, 1000),
				'Col B': np.random.normal(0, 1, 1000)})

# Overlapping Histograms
alt.Chart(pd.melt(df,
				id_vars=df.index.name,
				value_vars=df.columns,
				var_name='Columns',
				value_name='Values')
		).mark_area(opacity=0.5,
					interpolate='step'
					).encode(
	alt.X('Values', bin=alt.Bin(maxbins=10)),
	alt.Y('count()', stack=None),
	alt.Color('Columns')
).add_selection(alt.selection_interval(encodings=['x']))
