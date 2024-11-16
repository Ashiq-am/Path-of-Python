from IPython.display import display, HTML

import pandas as pd
import numpy as np

dict = {'Name':['Martha', 'Tim', 'Rob', 'Georgia'],
		'Maths':[87, 91, 97, 95],
		'Science':[83, 99, 84, 76]
	}

df = pd.DataFrame(dict)

display(df)

df2 = {'Name': 'Amy', 'Maths': 89, 'Science': 93}
df = df.append(df2, ignore_index = True)

display(df)
