emp_df = pd.read_csv(r'GFG.txt')

# split column data on basis of seperator
# convert it into list using to_list
# stack method performs transpose operation
# to the data
emp_df1 = pd.DataFrame(emp_df.name.str.split('|').to_list(),
					index = emp_df.dept).stack()

emp_df1 = emp_df1.reset_index([0, 'dept'])
emp_df1.columns =['Dept', 'Name']

emp_df1
