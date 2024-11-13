# Python program to check if all
# elements in a List are same

def chkList(lst):
	return len(set(lst)) == 1


# Driver Code
lst = ['Geeks', 'Geeks', 'Geeks', 'Geeks']

if chkList(lst) == True: print("Equal")
else: print("Not Equal")
