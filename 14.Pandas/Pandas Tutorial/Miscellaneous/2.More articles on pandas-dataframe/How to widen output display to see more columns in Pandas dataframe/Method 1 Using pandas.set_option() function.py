# importing numpy library
import numpy as np

# importing pandas library
import pandas as pd

# define a dataframe of
# 2 rows and 100 columns
# with random entries
df = pd.DataFrame(np.random.random(200).reshape(2, 100))

# show the dataframe
df
