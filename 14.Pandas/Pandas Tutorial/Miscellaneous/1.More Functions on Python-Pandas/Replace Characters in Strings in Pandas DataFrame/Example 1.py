# import pandas
import pandas as pd

data = {'Student_Full_Name': ['Mukul_Jatav', 'Rahul_Shukla',
							'Robin_Singh', 'Mayank_Sharma',
							'Akash_Verma'],
		'Father_Full_name': ['Mukesh_Jatav', 'Siddhart_Shukla',
							'Rohit_Singh', 'Sunil_Sharma',
							'Rajesh_Verma']
		}
# create an dataframe
df = pd.DataFrame(data, columns=['Student_Full_Name',
								'Father_Full_name'])

# print dataframe
print(" original dataframe \n", df)

# replace '_' with '-'
df = df.replace('_', '+', regex=True)

# print dataframe
print(" After replace character \n", df)
