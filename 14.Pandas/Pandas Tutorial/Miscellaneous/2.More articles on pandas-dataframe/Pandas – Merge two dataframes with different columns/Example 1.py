# importing pandas module
import pandas as pd


# dictionary with list object in
# values ie college details
details = {
	'Name': ['Sravan', 'Sai', 'Mohan', 'Ishitha'],
	'College': ['Vignan', 'Vignan', 'Vignan', 'Vignan'],
	'Physics': [99, 76, 71, 93],
	'Chemistry': [97, 67, 65, 89],
	'Data Science': [93, 65, 65, 85]
}


# converting to dataframe using DataFrame()
df = pd.DataFrame(details)


# print data frame
df
