# importing pandas as pd
import pandas as pd

# Creating the multi-index form tuples
midx = pd.MultiIndex.from_tuples([('Sam', 21), ('Norah', 25), ('Jessica', 32),
									('Irwin', 24)], names =['Name', 'Age'])

# Print the Multi-Index
midx
