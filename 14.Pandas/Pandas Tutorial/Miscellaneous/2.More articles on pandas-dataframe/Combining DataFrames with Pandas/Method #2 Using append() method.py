# import required module
import pandas as pd

# making a dataset
data1 = {
	'Serial_No.': ['1', '2', '3', '4', '5'],
	'First': ['F0', 'F1', 'F2', 'F3', 'F4'],
	'Second': ['S0', 'S1', 'S2', 'S3', 'S4'],
}

# creating a dataframe
df1 = pd.DataFrame(data1, columns=['Serial_No.',
								'First',
								'Second'])

# display dataframe
df1


# making a dataset
data2 = {
	'Serial_No.': ['6', '7', '8', '9', '10'],
	'First': ['F10', 'F11', 'F12', 'F13', 'F14'],
	'Second': ['S10', 'S11', 'S12', 'S13', 'S14'],
}

# creating a dataset
df2 = pd.DataFrame(data2, columns=['Serial_No.',
								'First',
								'Second'])

# display dataset
df2
