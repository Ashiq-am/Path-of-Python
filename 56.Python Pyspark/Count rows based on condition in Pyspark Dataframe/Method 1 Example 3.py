# condition to get rows in dataframe
# where ID not equal to 1 and name is sridevi
print('Total rows in dataframe where ID \
not equal to 1 and name is sridevi')
print(dataframe.where((dataframe.ID != '1') &
					(dataframe.NAME == 'sridevi')
					).count())

# condition to get rows in dataframe
# where college is equal to vignan or iit
print('Total rows in dataframe where college is\
vignan or iit with where clause')
print(dataframe.where((dataframe.college == 'vignan') |
					(dataframe.college == 'iit')).count())
