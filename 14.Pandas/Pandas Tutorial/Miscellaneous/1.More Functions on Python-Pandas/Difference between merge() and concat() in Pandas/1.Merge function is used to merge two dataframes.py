import pandas as pd

df1 = pd.DataFrame({'Roll Number': [101, 102, 103],'Name': ['Alice', 'Bob', 'Charlie'],'Marks': [85, 92, 78]})
df2 = pd.DataFrame({'Roll Number': [101, 102, 103],'Subject': ['Math', 'Science', 'English']})

# Merging the two DataFrames on 'Roll Number'
merged_df = pd.merge(df1, df2, on='Roll Number', how='inner')
print(merged_df)