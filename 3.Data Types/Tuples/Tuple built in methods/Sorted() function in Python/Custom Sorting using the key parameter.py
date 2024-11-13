L = ["cccc", "b", "dd", "aaa"]

print ("Normal sort :", sorted(L))

print ("Sort with len :", sorted(L, key = len))













'''Key also takes user-defined functions as its value for the basis of sorting.'''






# Sort a list of integers based on
# their remainder on dividing from 7

def func(x):
	return x % 7

L = [15, 3, 11, 7]

print ("Normal sort :", sorted(L))
print ("Sorted with key:", sorted(L, key = func))
