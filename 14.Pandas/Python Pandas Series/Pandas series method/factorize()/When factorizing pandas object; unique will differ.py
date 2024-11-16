# When factorizing pandas object; unique will differ
from turtle import pd

a = pd.Categorical(['a', 'a', 'c'], categories =['a', 'b', 'c'])

label3, unique3 = pd.factorize(a)

print("\n\nNumeric Representation : \n", label3)
print("Unique Values : \n", unique3)
