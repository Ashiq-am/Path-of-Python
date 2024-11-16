# import required module
import pandas as pd

# create dataframe
df = pd.DataFrame({'Animal': ['Falcon', 'Falcon', 'Parrot', 'Parrot'],
				'Max Speed': [380., 370., 24., 26.]})

# use groupby() to compute sum
df.groupby(['Animal']).sum()
