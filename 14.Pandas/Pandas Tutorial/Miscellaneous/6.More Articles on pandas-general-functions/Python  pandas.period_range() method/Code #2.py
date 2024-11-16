# importing pandas as pd
import pandas as pd

# period_range with freq = day
per1 = pd.period_range(start ='2018-12-20',
			end ='2019-01-01', freq ='D')

for val in per1:
	print(val)
