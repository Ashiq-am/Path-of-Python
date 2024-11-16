# importing pandas as pd
import pandas as pd

# Creating a dictionary
d = {'id':['1', '2', '3'],
	'Column 1.1':[14, 15, 16],
	'Column 1.2':[10, 10, 10],
	'Column 1.3':[1, 4, 5],
	'Column 2.1':[1, 2, 3],
	'Column 2.2':[10, 10, 10], }

# Converting dictionary into a data-frame
df = pd.DataFrame(d)
print(df)
