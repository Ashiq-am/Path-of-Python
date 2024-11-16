import numpy as np
import pandas as pd

def diff(a, b):
	return b - a

data = np.arange(0, 20).reshape(4, 5)


df = pd.DataFrame(data,
				index=['Row 1', 'Row 2', 'Row 3', 'Row 4'],
				columns=['Column 1', 'Column 2', 'Column 3',
						'Column 4', 'Column 5'])


df['Difference_2_1'] = df.apply(
	lambda x: diff(x['Column 2'], x['Column 2']), axis=1)
