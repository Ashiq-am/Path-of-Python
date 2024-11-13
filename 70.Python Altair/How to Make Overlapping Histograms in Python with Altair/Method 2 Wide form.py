# importing libraries
import pandas as pd
import altair as alt
import numpy as np


np.random.seed(42)

# creating data
df = pd.DataFrame({'Col 1': np.random.normal(-1, 1, 1000),
				'Col 2': np.random.normal(0, 1, 1000)})

# Overlapping Histograms
alt.Chart(df).transform_fold(
	['Col 1', 'Col 2'],
	as_=['Columns', 'Values']
).mark_area(
	opacity=0.5,
	interpolate='step'
).encode(
	alt.X('Values:Q', bin=alt.Bin(maxbins=100)),
	alt.Y('count()', stack=None),
	alt.Color('Columns:N')
)
