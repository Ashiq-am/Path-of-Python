# condition to get rows in dataframe
# where ID not equal to 1
print('Total rows in dataframe where\
ID except 1 with where clause')

print(dataframe.where(dataframe.ID != '1').count())

# condition to get rows in dataframe
# where college is equal to vignan
print('Total rows in dataframe where\
college is vignan with where clause')
print(dataframe.where(dataframe.college == 'vignan').count())


# condition to get rows in dataframe
# where id greater than 2
print('Total rows in dataframe where ID greater\
than 2 with where clause')
print(dataframe.where(dataframe.ID > 2).count())
