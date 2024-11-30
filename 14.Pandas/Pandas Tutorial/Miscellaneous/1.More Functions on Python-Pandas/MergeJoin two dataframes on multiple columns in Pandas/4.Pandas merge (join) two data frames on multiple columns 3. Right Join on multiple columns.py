import pandas as pd

df1 = pd.DataFrame({'EmployeeID': [101, 102, 103],'Department': ['HR', 'Finance', 'IT'],'Salary': [70000, 80000, 90000]})
df2 = pd.DataFrame({'EmployeeID': [101, 102, 104],'Department': ['HR', 'Finance', 'IT'],'Bonus': [5000, 6000, 7000]})

result_left = pd.merge(df1, df2, on=['EmployeeID', 'Department'], how='right')
print("\nRight Join Example:")
print(result_left)