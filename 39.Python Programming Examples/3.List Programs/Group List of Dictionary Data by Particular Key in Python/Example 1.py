# import a groupby() method
# from itertools module
from itertools import groupby

# dictionary
INFO = [
	{'employee': 'XYZ_1', 'company': 'ABC_1'},
	{'employee': 'XYZ_2', 'company': 'ABC_2'},
	{'employee': 'XYZ_3', 'company': 'ABC_3'},
	{'employee': 'XYZ_4', 'company': 'ABC_3'},
	{'employee': 'XYZ_5', 'company': 'ABC_2'},
	{'employee': 'XYZ_6', 'company': 'ABC_3'},
	{'employee': 'XYZ_7', 'company': 'ABC_1'},
	{'employee': 'XYZ_8', 'company': 'ABC_2'},
	{'employee': 'XYZ_9', 'company': 'ABC_1'}
]


# define a fuction for key
def key_func(k):
	return k['company']

# sort INFO data by 'company' key.
INFO = sorted(INFO, key=key_func)

for key, value in groupby(INFO, key_func):
	print(key)
	print(list(value))
