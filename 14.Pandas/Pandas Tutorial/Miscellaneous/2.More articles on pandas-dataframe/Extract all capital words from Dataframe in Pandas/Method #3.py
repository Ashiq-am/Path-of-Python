# Import required modules
import re
import pandas


# Create dataset
data = [['tom', 'DATAFRAME', '200.00'],
		['PANDAS', 15, 3.14],
		['r2j', 14, 'PYTHON']]

# Create the pandas DataFrame
df = pandas.DataFrame(data)


# access each element in the dataframe
for i in range(df.shape[1]):
    for ele in df[i]:
        if bool(re.match(r'\w*[A-Z]\w*', str(ele))):
            print(ele)
