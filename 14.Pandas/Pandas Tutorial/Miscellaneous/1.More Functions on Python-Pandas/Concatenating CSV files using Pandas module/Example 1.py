#import pandas
import pandas as pd

# read Employee file
employee_df = pd.read_csv('Employee.csv')

# print employee records
print(employee_df)

# read Updated file
updated_df = pd.read_csv('Updated.csv')

# print updated records
print(updated_df)

# form new dataframe by combining both employee_df and updated_df
# concat method appends records of updated_df to employee_df
# drop_duplicates method drop rows having same emp_id keeping
# only the latest insertions
# resets the index to 0
final_dataframe = pd.concat([employee_df, updated_df]).drop_duplicates(
	subset='emp_id', keep='last').reset_index(drop=True)

# print old,new and updates records
print(final_dataframe)

# export all records to a new csv file
final_dataframe.to_csv('Updated_Employees.csv', index=False)
