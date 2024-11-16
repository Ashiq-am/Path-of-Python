import pandas as pd
import numpy as np


dict = {'Name': ['Martha', 'Tim', 'Rob', 'Georgia'],
		'Maths': [87, 91, 97, 95],
		'Science': [83, 99, 84, 76]
		}

df1 = pd.DataFrame(dict)

dict = {'Name': ['Amy', 'Maddy'],
		'Maths': [89, 90],
		'Science': [93, 81]
		}

df2 = pd.DataFrame(dict)

dict = {'Name': ['Rob', 'Rick', 'Anish'],
		'Maths': [89, 90, 87],
		'Science': [93, 81, 90]
		}

df3 = pd.DataFrame(dict)

# Concating Dataframes
df = pd.concat([df1, df2, df3],
			keys=['t1', 't2', 't3'])
display(df)

df = pd.concat([df1, df2, df3],
			keys=['t1', 't2', 't3']).reset_index()
display(df)
