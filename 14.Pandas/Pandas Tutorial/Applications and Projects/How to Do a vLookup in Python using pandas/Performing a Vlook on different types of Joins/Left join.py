# import pandas
import pandas as pd

# read csv data
df1 = pd.read_csv('Student_data.csv')
df2 = pd.read_csv('Course_enrolled.csv')

Left_join = pd.merge(df1,
					df2,
					on ='Name',
					how ='left')
Left_join
