# import pandas as pd
import pandas as pd

# list of strings
lst = [[1, 'Geeks'], [2, 'For'], [3, 'Geeks']]

# Calling DataFrame constructor
# on list with column names
print(pd.DataFrame(lst, columns=['Id', 'Data']))
