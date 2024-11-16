import pandas as pd
import numpy as np

# Creating the Data frame through series
# and specifying datatype along with it
df = pd.DataFrame({"Column_1": pd.Series([1, 2, 3], dtype=np.dtype("int32")),
                   # Column_1 datatype is int32

                   "Column_2": pd.Series(["Apple", "Ball", "Cat"],
                                         dtype=np.dtype("object")),
                   # Column_2 datatype is 0

                   "Column_3": pd.Series([True, False, np.nan],
                                         dtype=np.dtype("object")),
                   # Column_3 datatype is 0

                   "Column_4": pd.Series([10, np.nan, 20],
                                         dtype=np.dtype("float")),
                   # Column_4 datatype is float

                   "Column_5": pd.Series([np.nan, 100.5, 200],
                                         dtype=np.dtype("float"))})
# Column_5 datatype is float

# printing dataframe
print("PRINTING DATAFRAME")
display(df)

# checking datatype
print()
print("CHECKING DATATYPE")
print(df.dtypes)

# convert datatype
print()
print("AFTER DATATYPE CONVERSION")
print(df.convert_dtypes().dtypes)
