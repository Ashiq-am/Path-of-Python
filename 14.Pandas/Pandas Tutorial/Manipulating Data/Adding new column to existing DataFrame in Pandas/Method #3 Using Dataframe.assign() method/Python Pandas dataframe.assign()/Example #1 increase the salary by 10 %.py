# increase the salary by 10 %
from pandas.tests.groupby.test_value_counts import df

df.assign(Revised_Salary = lambda x: df['Salary']
							+ df['Salary']/10)
