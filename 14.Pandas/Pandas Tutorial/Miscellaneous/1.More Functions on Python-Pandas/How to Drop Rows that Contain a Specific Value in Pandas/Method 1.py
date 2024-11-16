# import pandas module
import pandas as pd

# create dataframe with 4 columns
data = pd.DataFrame({

	"name": ['sravan', 'jyothika', 'harsha', 'ramya',
			'sravan', 'jyothika', 'harsha', 'ramya',
			'sravan', 'jyothika', 'harsha', 'ramya'],
	"subjects": ['java', 'java', 'java', 'python',
				'python', 'python', 'html/php', 'html/php',
				'html/php', 'php/js', 'php/js', 'php/js'],
	"marks": [98, 79, 89, 97, 82, 98, 90,
			87, 78, 89, 93, 94]
})

# display
print(data)

print("---------------")

# drop rows where value is 98
# by using not equal operator
print(data[data.marks != 98])

print("---------------")
