# importing pandas as pd
import pandas as pd

per1 = pd.date_range(start ='1-1-2018',
		end ='1-05-2018', freq ='5H')

for val in per1:
	print(val)
