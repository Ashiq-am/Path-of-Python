''

'''

# Python program to check if frequency of 
# all characters of a string are unique 
	
	# creating a frequency array 
	freq =[0]*26
	
	# Finding length of s 
	n = len(s) 
	
	for i in range(n): 
	
		# counting frequency of all characters 
		freq[ord(s[i])-97] += 1

	# sorting the frequency array 
	freq.sort() 
	for i in range(25): 
	
		# checking if element is zero 
		if (freq[i] == 0): 
			continue

		# if element is non-zero 
		# checking if frequencies are unique 
		if (freq[i] == freq[i + 1]): 
			return False

	return True
	
# Driver code 
s ="abaccc"

if(check(s)): 
	print("Yes") 
else: 
	print("No") 
	
	
'''


