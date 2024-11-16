import pandas as pd
import numpy as np


# dictionary
diff = pd.DataFrame({'R': ['a', 'c', 'd'],
					'T': ['d', 'a', 'c'],
					'S_': [1, 2, 3]})

print(pd.get_dummies(diff, prefix=['column1', 'column2']))
