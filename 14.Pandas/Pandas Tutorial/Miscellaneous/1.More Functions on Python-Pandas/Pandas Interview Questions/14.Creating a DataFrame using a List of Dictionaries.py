# import pandas as pd
import pandas as pd

# list of strings
lst = [{1: 'Geeks', 2: 'For', 3: 'Geeks'},
{1: 'Portal', 2: 'for', 3: 'Geeks'}]

# Calling DataFrame constructor on list
print(pd.DataFrame(lst))
