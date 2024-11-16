# importing pandas as pd
import pandas as pd

# Calling with pd.Period
per = pd.period_range(start = pd.Period('2017Q1', freq ='Q'),
				end = pd.Period('2018Q2', freq ='Q'), freq ='M')

for val in per:
	print(val)
