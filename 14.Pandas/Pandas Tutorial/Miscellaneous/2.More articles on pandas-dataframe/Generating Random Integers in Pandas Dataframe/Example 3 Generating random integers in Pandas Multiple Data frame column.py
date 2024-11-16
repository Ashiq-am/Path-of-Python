# importing pandas and numpy libraries
import numpy as np
import pandas as pd

# generating 12X3 i.e 36 random integers from 5 to 40
data = np.random.randint(5, 40, size = (12, 3))
df = pd.DataFrame(data, columns = ['random_no_1',
								'random_no_2',
								'random_no_3'])

# displaying random integers in the dataframe
print(df)
