# importing the module
import numpy as np

# displaying the datatypes
display(df.dtypes)

# converting 'Field_2' from float to int
df['Field_2'] = df['Field_2'].apply(np.int64)

# displaying the datatypes
display(df.dtypes)
