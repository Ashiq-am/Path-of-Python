# importing the required packaged
# in python
import pandas as pd
import os

dir_name = "csvfoldergfg"

# specifying an empty list for content
content = []
for file in os.listdir(dir_name):
    # reading content into data frame
    df = pd.read_csv(file)
    df_list.append(df)

final_content = df.append(df for df in df_list)
print(final_content)
