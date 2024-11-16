import pandas as pd

data = {'A': [45, 37, 42, 50],
        'B': ['R', 'O', 'M', 'Y'],
        'C': [56, 67, 68, 60],

        }

df = pd.DataFrame(data)

corrM = df.corr()
corrM
