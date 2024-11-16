from turtle import pd

new_row = pd.DataFrame({'Name':'Geeks', 'Team':'Boston', 'Number':3,
						'Position':'PG', 'Age':33, 'Height':'6-2',
						'Weight':189, 'College':'MIT', 'Salary':99999},
															index =[0])
# simply concatenate both dataframes
df = pd.concat([new_row, df]).reset_index(drop = True)
df.head(5)
