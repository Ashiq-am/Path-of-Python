# import pandas module
import pandas as pd

# create dataframe with 4 columns
data = pd.DataFrame({

	"name": ['sravan', 'jyothika', 'harsha',
			'ramya', 'sravan', 'jyothika',
			'harsha', 'ramya', 'sravan', 'jyothika',
			'harsha', 'ramya'],
	"subjects": ['java', 'java', 'java', 'python',
				'python', 'python', 'html/php',
				'html/php', 'html/php', 'php/js',
				'php/js', 'php/js'],
	"internal marks": [98, 79, 89, 97, 82, 98, 90,
					87, 78, 89, 93, 94],
	"external marks": [88, 71, 89, 97, 82, 98, 80,
					87, 71, 89, 92, 64],
})

# display dataframe
print(data)
