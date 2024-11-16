#import pandas
import pandas as pd

# read Employee file
df1 = pd.read_csv('gfg1.csv')

# print employee records
print('\ngfg1.csv:\n', df1)

# read Updated file
df2 = pd.read_csv('gfg2.csv')

# print updated records
print('\ngfg2.csv:\n', df2)

# form new dataframe by combining both employee_df
# and updated_df concat method appends records of
# updated_df to employee_df drop_duplicates method
# drop rows having same emp_id keeping only the
# latest insertions resets the index to 0
final_df = pd.concat([df1, df2]).drop_duplicates(subset='ORGANIZATION').reset_index(drop=True)

# print old,new and updates records
print('\ngfg3.csv:\n', final_df)

# export all records to a new csv file
final_df.to_csv('gfg3.csv', index=False)
