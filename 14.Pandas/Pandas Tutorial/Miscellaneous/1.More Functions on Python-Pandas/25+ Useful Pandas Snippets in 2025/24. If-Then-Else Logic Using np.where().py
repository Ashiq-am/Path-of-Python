import numpy as np
df['new_col'] = np.where(df['col1'] > 0, 'Positive', 'Negative')
