import pandas as pd
import numpy as np

# create DataFrame
dframe = pd.DataFrame({'Geeks': [23, 24, 22, 22, 23, 24],
						'For': [10, 12, 13, 14, 15, 16],
						'geeks': [122, 142, 112, 122, 114, 112]},
						columns = ['Geeks', 'For', 'geeks'])

# Apply groupby and aggregate function
# max to find max value of column

# &quot;For&quot; and column &quot;geeks&quot; for every
# different value of column &quot;Geeks&quot;.

print(dframe.groupby(['Geeks']).max())
