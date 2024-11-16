#import pandas
import pandas

# create dataframe
data = pandas.DataFrame({'name': ['sireesha', 'priyank',
								'ojaswi', 'gnanesh'],
						'subjects': ['java', 'networks',
									'c', 'c#']})

# consider a list
list1 = ['sireesha', 'priyank']

# check the pandas name column
# contain the given list if strings
print(data[data['name'].isin(list1)])

# consider a list
list2 = ['java', 'c']

# check the pandas subjects column
# contain the given list if strings
print(data[data['subjects'].isin(list2)])
