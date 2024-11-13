numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(numbers)

# passing an element that is not in set
# this will throw an KeyError exception
try:
	numbers.remove(13)
except Exception as e:
	print("KeyError Exception raised")
	print(e, "is not present in the set")

# printing the resultant set
print("\nresultant set : ", numbers)
