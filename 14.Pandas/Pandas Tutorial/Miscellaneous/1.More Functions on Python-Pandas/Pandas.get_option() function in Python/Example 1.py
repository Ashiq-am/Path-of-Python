# importing the module
import pandas as pd

# fetching maximum number of
# columns that can be diplayed
print("The value of max_columns : " + str(pd.get_option("display.max_columns")))

# fetching maximum number of
# rows that can be diplayed
print("The value of max_rows : " + str(pd.get_option("display.max_rows")))

# fetching minimum number of
# rows that can be diplayed
print("The value of min_rows : " + str(pd.get_option("display.min_rows")))
