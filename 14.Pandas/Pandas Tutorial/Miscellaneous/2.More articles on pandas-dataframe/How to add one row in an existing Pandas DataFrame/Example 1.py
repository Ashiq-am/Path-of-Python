from IPython.display import display, HTML

import pandas as pd
from numpy.random import randint

dict = {'Name':['Martha', 'Tim', 'Rob', 'Georgia'],
		'Maths':[87, 91, 97, 95],
		'Science':[83, 99, 84, 76]
	}

df = pd.DataFrame(dict)

display(df)

df.loc[len(df.index)] = ['Amy', 89, 93]

display(df)
