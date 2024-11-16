# importing pandas and numpy libraries
import numpy as np
import pandas as pd

# generating 11 random integers from 5 to 35
data = np.random.randint(5, 35, size = 11)
df = pd.DataFrame(data, columns = ['random_numbers'])

# displaying random integers in data frame
print(df)
