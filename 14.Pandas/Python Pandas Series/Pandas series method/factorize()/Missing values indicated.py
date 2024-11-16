# Missing values indicated
from turtle import pd

label2, unique2 = pd.factorize(['b', None, 'd', 'c', None, 'a', ],
											na_sentinel = -101)

print("\n\nNumeric Representation : \n", label2)
print("Unique Values : \n", unique2)
