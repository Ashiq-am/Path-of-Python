import pandas as pd
import numpy as np


df= pd.DataFrame({'number': np.random.randint(1, 100, 10)})
df['bins'] = pd.cut(x=df['number'], bins=[1, 20, 40, 60,
										80, 100])
print(df)

# We can check the frequency of each bin
print(df['bins'].unique())
