#importing pandas module
import pandas as pd

#creating dataframe with 2 columns
df = pd.DataFrame(data=[[[ 300, 400, 500, 600], 'sravan_payment'],
						[[ 300, 322, 333, 233], 'bobby_payment']],
				index=[ 0, 1], columns=[ 'A', 'B'])

display(df)
