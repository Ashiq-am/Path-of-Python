import pandas as pd
import numpy as np

# creating a dataframe
df = pd.DataFrame({"Roll_No.": ([1, 2, 3]),
				"Name": ["Raj", "Ritu", "Rohan"],
				"Result": ["Pass", "Fail", np.nan],
				"Promoted": [True, False, np.nan],
				"Marks": [90.33, 30.6, np.nan]})

# printing the dataframe
print("PRINTING DATAFRAME")
display(df)

# checking datatype
print()
print("PRINTING DATATYPE")
print(df.dtypes)

# converting datatype
print()
print("AFTER CONVERTING DATATYPE")
print(df.convert_dtypes().dtypes)
