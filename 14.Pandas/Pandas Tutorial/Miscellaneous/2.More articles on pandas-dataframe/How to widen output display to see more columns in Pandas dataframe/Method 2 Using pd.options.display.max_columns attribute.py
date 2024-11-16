# importing numpy library
import numpy as np

# importing pandas library
import pandas as pd

# define a dataframe of
# 15 rows and 200 columns
# with random entries
df = pd.DataFrame(np.random.randint(0, 100,
									size =(15, 200)))

# show the dataframe
df
