# import pandas module
import pandas as pd

# specify the start date is 2021 jan 1 st
# specify the emd date is 2021 feb 1 st
a = pd.date_range(start='1/1/2021', end='2/1/2021')

# display only date using date() function
for i in a:
	print(i.date())
