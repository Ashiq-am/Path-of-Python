# Import pandas library
import pandas

# Create dataset
data = [['tom', 'DATAFRAME', '200.00'],
        ['PANDAS', 15, 3.14],
        ['r2j', 14, 'PYTHON']]

# Create the pandas DataFrame
df = pandas.DataFrame(data)

# access each elemnet in the dataframe
for i in range(df.shape[1]):
    for ele in df[i]:

        # use isupper()
        if str(ele).isupper():
            print(ele)
