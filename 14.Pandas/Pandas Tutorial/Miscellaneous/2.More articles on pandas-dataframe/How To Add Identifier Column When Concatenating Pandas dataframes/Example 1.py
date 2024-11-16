import pandas as pd
import numpy as np


dict = {'Name':['Martha', 'Tim', 'Rob', 'Georgia'],
		'Maths':[87, 91, 97, 95],
		'Science':[83, 99, 84, 76]
	}

df1 = pd.DataFrame(dict)

dict = {'Name':['Amy', 'Maddy'],
		'Maths':[89, 90],
		'Science':[93, 81]
	}

df2 = pd.DataFrame(dict)

# Concatinating two dataframes
df = pd.concat([df1,df2],keys=['t1', 't2'])
display(df)

df = pd.concat([df1,df2], keys=['t1', 't2']).reset_index()
display(df)
