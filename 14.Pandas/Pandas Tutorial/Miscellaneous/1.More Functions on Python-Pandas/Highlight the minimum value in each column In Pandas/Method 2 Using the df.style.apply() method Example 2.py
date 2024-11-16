# Defining custom function
# which returns the list for
# df.style.apply() method
from pandas.tests.groupby.test_value_counts import df


def highlight_min(s):
    is_min = s == s.min()

    return ['background: lightgreen' if cell else ''
            for cell in is_min]


df.style.apply(highlight_min)
