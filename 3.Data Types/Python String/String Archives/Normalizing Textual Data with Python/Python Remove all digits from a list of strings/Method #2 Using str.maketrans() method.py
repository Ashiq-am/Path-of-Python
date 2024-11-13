# Python program to Remove all
# digits from a list of string
from string import digits

def remove(list):
	remove_digits = str.maketrans('', '', digits)
	list = [i.translate(remove_digits) for i in list]
	return list

# Driver code

list = ['4geeks', '3for', '4geeks']
print(remove(list))
