# importing pandas as pd
import pandas as pd

# period_range with freq = day
per1 = pd.period_range(start ='2018-12-20',
			end ='2019-01-01', freq ='D')

# period_range with freq = month
per2 = pd.period_range(start ='2018-12-20',
			end ='2019-12-01', freq ='M')

print(per1, "\n\n", per2)
