from IPython.display import display, HTML

import pandas as pd
import numpy as np

dict = {'Name':['Martha', 'Tim', 'Rob', 'Georgia'],
		'Maths':[87, 91, 97, 95],
		'Science':[83, 99, 84, 76]
	}

df1 = pd.DataFrame(dict)
display(df1)

dict = {'Name':['Amy', 'Maddy'],
		'Maths':[89, 90],
		'Science':[93, 81]
	}

df2 = pd.DataFrame(dict)
display(df2)

df3 = pd.concat([df1, df2], ignore_index = True)
df3.reset_index()

display(df3)
