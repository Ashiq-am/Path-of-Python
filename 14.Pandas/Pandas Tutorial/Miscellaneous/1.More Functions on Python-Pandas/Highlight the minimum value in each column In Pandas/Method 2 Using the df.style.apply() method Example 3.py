# Defining custom function
# which returns the list for
# df.style.apply() method
import numpy as np
from pandas.tests.groupby.test_value_counts import df


def highlight_min(s):
    if s.dtype == np.object:
        is_min = [False for _ in range(s.shape[0])]
    else:
        is_min = s == s.min()

    return ['background: lightgreen' if cell else ''
            for cell in is_min]


df.style.apply(highlight_min)
