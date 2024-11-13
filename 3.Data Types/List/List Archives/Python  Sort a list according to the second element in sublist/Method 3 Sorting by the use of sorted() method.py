# Python code to sort the tuples using second element
# of sublist Function to sort using sorted()
def Sort(sub_li):

	# reverse = None (Sorts in Ascending order)
	# key is set to sort using second element of
	# sublist lambda has been used
	return(sorted(sub_li, key = lambda x: x[1]))

# Driver Code
sub_li =[['rishav', 10], ['akash', 5], ['ram', 20], ['gaurav', 15]]
print(Sort(sub_li))
