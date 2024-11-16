# Conversion can be done using astype()
from turtle import pd

df3 = pd.DataFrame({'A': list('efgh'), 'B': list('aebc')})
print ("\n\ndf3 : \n", df3)
print("\ndf3 type :\n", df3.dtypes)

df4 = df3.astype('category')
print ("\n\ndf4 type:\n", df4.dtypes)
