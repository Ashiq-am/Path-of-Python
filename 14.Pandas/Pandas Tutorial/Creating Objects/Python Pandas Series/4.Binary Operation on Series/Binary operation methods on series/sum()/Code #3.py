# importing pandas module
import pandas as pd

# making a dict of list
data = {'name': ['John', 'Peter', 'Karl'],
        'age': [23, 42, 19]}

val = pd.DataFrame(data)

# sum of all salary
val['total'] = val['age'].sum()

val
