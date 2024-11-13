# import required modules
import altair as alt
import numpy as np
import pandas as pd

# generating data
np.random.seed(42)
df = pd.DataFrame({'height': np.random.normal(150, 10, 1000)})

# initialize chart
base = alt.Chart(df)

# generate histogram
hist = base.mark_bar().encode(
	x=alt.X('height:Q', bin=alt.BinParams(maxbins=100), axis=None), y='count()')

# generate median line
red_median_line = base.mark_rule(color='red').encode(
	x=alt.X('mean(height):Q', title='Height'), size=alt.value(5))

# depict illustration
hist+red_median_line
