# condition to get rows in dataframe
# where ID =1
print('Total rows in dataframe where\
ID = 1 with where clause')
print(dataframe.where(dataframe.ID == '1').count())

print('They are ')
dataframe.where(dataframe.ID == '1').show()
