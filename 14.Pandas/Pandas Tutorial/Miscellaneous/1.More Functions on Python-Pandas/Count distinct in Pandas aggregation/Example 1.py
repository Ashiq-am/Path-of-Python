# import module
import pandas as pd
import numpy as np

# create Data frame
df = pd.DataFrame({'Video_Upload_Date': ['2020-01-17',
										'2020-01-17',
										'2020-01-19',
										'2020-01-19',
										'2020-01-19'],
				'Viewer_Id': ['031', '031', '032',
								'032', '032'],
				'Watch_Time': [34, 43, 43, 41, 40]})

# print original Dataframe
print(df)

# let's Count distinct in Pandas aggregation
df = df.groupby("Video_Upload_Date").agg(
	{"Watch_Time": np.sum, "Viewer_Id": pd.Series.nunique})

# print final output
print(df)
