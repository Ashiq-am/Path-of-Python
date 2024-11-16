import numpy as np
import pandas as pd

data = np.arange(0, 20).reshape(4, 5)


df1 = pd.DataFrame(data,
				index=['Row 1', 'Row 2', 'Row 3', 'Row 4'],
				columns=['Column 1', 'Column 2', 'Column 3',
							'Column 4', 'Column 5'])

# using our previous example
# now let's subtract the values of two columns
df1['Column 1'] - df1['Column 2']
