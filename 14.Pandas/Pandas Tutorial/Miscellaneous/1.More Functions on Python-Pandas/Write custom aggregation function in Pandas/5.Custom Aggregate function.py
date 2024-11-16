# import pandas library
import pandas as pd

# Creating DataFrame
df = pd.DataFrame(
	{'stud_id' : [101, 102, 103, 104,
				101, 102, 103, 104],
	'sub_code' : ['CSE6001', 'CSE6001', 'CSE6001',
				'CSE6001', 'CSE6002', 'CSE6002',
				'CSE6002', 'CSE6002'],
	'marks' : [77, 86, 55, 90,
				65, 90, 80, 67]}
)

# Printing DataFrame
df
