# Python code demonstrate creating
# DataFrame from dict narray / lists
# By default addresses.

import pandas as pd

# intialise data of lists.
data = {'Category':['Array', 'Stack', 'Queue'],
		'Student_1':[20, 21, 19], 'Student_2':[15, 20, 14]}

# Create DataFrame
df = pd.DataFrame(data)

# Print the output.
print(df.transpose())
