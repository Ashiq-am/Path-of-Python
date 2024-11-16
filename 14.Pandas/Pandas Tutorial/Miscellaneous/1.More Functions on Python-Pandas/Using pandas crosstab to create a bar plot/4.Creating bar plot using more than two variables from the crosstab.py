# importing the module
import pandas as pd

# reading the csv file
df = pd.read_csv('Data.csv')

# Crosstab with three varibales
crosstb = pd.crosstab(df.Sex, [df.Nationality,
							df.Handedness])

# Bar ploting
a = crosstb.plot(kind='bar', rot=0)
a.legend(title='Handedness', bbox_to_anchor=(1, 1.02),
		loc='upper left')
