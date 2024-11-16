# Converting dataframe to category
from turtle import pd

df2 = pd.DataFrame({'A': list('1245'), 'B': list('3456')}, dtype ="category")

print ("df2 : \n", df2)
print("\n\ndf2 type :\n", df2.dtypes)

print ("\n\ndf2 column 0 :\n", df2['A'])
print ("\n\ndf2 column 1 :\n", df2['B'])
