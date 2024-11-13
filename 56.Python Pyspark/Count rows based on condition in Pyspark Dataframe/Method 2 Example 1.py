# condition to get rows in
# dataframe where ID =1
print('Total rows in dataframe where ID = 1 with filter clause')
print(dataframe.filter(dataframe.ID == '1').count())

print('They are ')
dataframe.filter(dataframe.ID == '1').show()
