# importing the module
import pandas as pd

# 'dd-mm-yyyy'
date_1 = '22-07-2011'
date_1 = pd.to_datetime(date_1, format ="%d-%m-%Y")

print("The day on the date " + str(date_1) +
	" is : " + date_1.day_name())

# 'mm.dd.yyyy'
date_2 = '12.03.2000'
date_2 = pd.to_datetime(date_2, format ="%m.%d.%Y")
print("The day on the date " + str(date_2) +
	" is : " + date_2.day_name())

# 'yyyy / dd / mm'
date_3 = '2004/9/4'
date_3 = pd.to_datetime(date_3, format ="%Y/%d/%m")
print("The day on the date " + str(date_2) +
	" is : " + date_3.day_name())
