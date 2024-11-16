import pandas as pd
import numpy as np

data = np.arange(0, 20).reshape(4, 5)


df = pd.DataFrame(data,
				index=['Row 1', 'Row 2', 'Row 3', 'Row 4'],
				columns=['Column 1', 'Column 2', 'Column 3',
						'Column 4', 'Column 5'])


df['diff_3_4'] = df.apply(lambda x: x['Column 3'] - x['Column 4'], axis=1)
df
