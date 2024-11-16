# import pandas library
import pandas as pd

# dictionary
d = {'ConsumerId': [1, 2, 3,
					4, 5],
	'CarName': ['I3', 'S4', 'J3',
				'Mini', 'Beetle'],
	'CompanyName': ['BMW','Mercedes', 'Jeep',
					'MiniCooper', 'Volkswagen'],
	'Price': [1200, 1400, 1500,
			1650, 1750]
	}

# create a dataframe
df = pd.DataFrame(d)

# show the dataframe
df
