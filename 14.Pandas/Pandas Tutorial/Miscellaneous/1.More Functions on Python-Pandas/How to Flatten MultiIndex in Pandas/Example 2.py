import pandas as pd

# create DataFrame muktiindexex
data = pd.MultiIndex.from_tuples([('Web Programming', 'php', 'sub1'),
								('Scripting', 'python', 'sub2'),
								('networks', 'computer network', 'sub3'),
								('architecture', 'computer organization', 'sub4'),
								('coding', 'java', 'sub5')],
								names=['Course', 'Subject name', 'subject id'])

# create dataframe with student marks

data = pd.DataFrame({'ravi': [98, 89, 90, 88, 93],
					'reshma': [78, 89, 80, 98, 63],
					'sahithi': [78, 89, 80, 98, 63]},
					index=data)


# flatten the index of all levels
data.reset_index(inplace=True)

# display
data
