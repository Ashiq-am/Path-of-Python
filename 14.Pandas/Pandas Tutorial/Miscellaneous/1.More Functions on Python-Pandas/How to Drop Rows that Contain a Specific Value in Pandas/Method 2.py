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
	"marks": [98, 79, 89, 97, 82, 98, 90, 87,
			78, 89, 93, 94]
})

# consider the list
list1 = [98, 82, 79]

# drop rows from above list
print(data[data.marks.isin(list1) == False])

print("---------------")

list2 = ['sravan', 'jyothika']
# drop rows from above list
print(data[data.name.isin(list2) == False])
