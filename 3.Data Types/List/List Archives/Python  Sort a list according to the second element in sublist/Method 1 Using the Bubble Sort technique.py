# Python code to sort the lists using the second element of sublists
# Inplace way to sort, use of third variable
def Sort(sub_li):
	l = len(sub_li)
	for i in range(0, l):
		for j in range(0, l-i-1):
			if (sub_li[j][1] > sub_li[j + 1][1]):
				tempo = sub_li[j]
				sub_li[j]= sub_li[j + 1]
				sub_li[j + 1]= tempo
	return sub_li

# Driver Code
sub_li =[['rishav', 10], ['akash', 5], ['ram', 20], ['gaurav', 15]]
print(Sort(sub_li))
