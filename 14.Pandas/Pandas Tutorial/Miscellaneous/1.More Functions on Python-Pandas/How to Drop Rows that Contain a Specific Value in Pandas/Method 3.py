# import pandas module
import pandas as pd

# create dataframe with 4 columns
data = pd.DataFrame({

	"name": ['sravan', 'jyothika', 'harsha', 'ramya',
			'sravan', 'jyothika', 'harsha', 'ramya',
			'sravan', 'jyothika', 'harsha', 'ramya'],
	"subjects": ['java', 'java', 'java', 'python',
				'python', 'python', 'html/php',
				'html/php', 'html/php', 'php/js',
				'php/js', 'php/js'],
	"marks": [98, 79, 89, 97, 82, 98, 90,
			87, 78, 89, 93, 94]
})

# drop specific values
# where marks is 98 and name is sravan
print(data[(data.marks != 98) & (data.name != 'sravan')])

print("------------------")

# drop specific values
# where marks is 98 or name is sravan
print(data[(data.marks != 98) | (data.name != 'sravan')])
