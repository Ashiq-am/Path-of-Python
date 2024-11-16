# Import pandas library
import pandas


# explict function to check if string
# contains only uppercase characters
def findCap(s):
	for ele in str(s):
		if ord(ele) < 65 or ord(ele) > 90:
			return 0
	return 1


# Create dataset
data = [['tom', 'DATAFRAME', '200.00'],
		['PANDAS', 15, 3.14],
		['r2j', 14, 'PYTHON']]

# Create the pandas DataFrame
df = pandas.DataFrame(data)


# access each element in
# the dataframe
for i in range(df.shape[1]):
	for ele in df[i]:

		# call explicit finction
		if findCap(ele):
			print(ele)
