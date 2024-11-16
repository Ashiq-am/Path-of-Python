# importing pandas library
import pandas as pd

# Initializing the nested list with Data set
player_list = [['20200712',50000,'20200812'],
			['20200714',51000,'20200814'],
			['20200716',51500,'20200816'],
			['20200719',53000,'20200819'],
			['20200721',54000,'20200821'],
			['20200724',55000,'20200824'],
			['20200729',57000,'20200824']]

# creating a pandas dataframe
df = pd.DataFrame(
player_list,columns = ['Treatment_start',
						'No.of Patients',
						'Treatment_end'])

# printing dataframe
print(df)
print()

# checking the type
print(df.dtypes)
