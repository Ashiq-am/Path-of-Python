import pandas as pd

# read the datasets
df1 = pd.read_csv(r"your_path/data_1.csv")
df2 = pd.read_csv(r"your_path/data_2.csv")

# print the datasets
print(df1.head())
print(df2.head())
concat_data = pd.concat([df1, df2], ignore_index=True)
print(concat_data)
