# Python code demonstrate creating
# DataFrame from dict narray / lists
# By default addresses.

import pandas as pd

# intialise data of lists.
data = {'Area':['Array', 'Stack', 'Queue'],
		'Student_1':[20, 21, 19], 'Student_2':[15, 20, 14]}

# Create DataFrame
df = pd.DataFrame(data, index =['Cat_1', 'Cat_2', 'Cat_3'])

# Print the output.
print(df)
