# sorting the numerics
from turtle import pd

label1, unique1 = pd.factorize(['b', 'd', 'd', 'c', 'a', 'c', 'a', 'b'],
														sort = True)

print("\n\nNumeric Representation : \n", label1)
print("Unique Values : \n", unique1)
