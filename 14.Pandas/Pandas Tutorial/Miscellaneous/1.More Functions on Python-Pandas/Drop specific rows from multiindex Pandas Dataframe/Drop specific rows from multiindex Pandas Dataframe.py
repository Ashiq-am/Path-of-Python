import numpy as np
import pandas as pd

mldx_arrays = [np.array(['lion', 'lion', 'lion', 'bison',
                         'bison', 'bison', 'hawk', 'hawk',
                         'hawk']),

               np.array(['height', 'weight', 'speed',
                         'height', 'weight', 'speed',
                         'height', 'weight', 'speed'])]

# creating a multi-index dataframe
# with random data
multiindex_df = pd.DataFrame(
    np.random.randn(9, 4), index=mldx_arrays,
    columns=['Type A', 'Type B', 'Type C', 'Type D'])

multiindex_df.index.names = ['level 0', 'level 1']
multiindex_df
