# importing pandas as pd
import pandas as pd

dRan1 = pd.date_range(start ='1-1-2018',
		end ='8-01-2018', freq ='M')

dRan2 = pd.date_range(start ='1-1-2018',
		end ='11-01-2018', freq ='3M')

print(dRan1, '\n\n', dRan2)
