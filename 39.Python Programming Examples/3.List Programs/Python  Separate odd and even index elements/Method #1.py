# Python3 code to demonstrate
# Separating odd and even index elements
# using naive method

# initializing list
test_list = [3, 6, 7, 8, 9, 2, 1, 5]

# printing original list
print("The original list : " + str(test_list))

# using naive method
# Separating odd and even index elements
odd_i = []
even_i = []
for i in range(0, len(test_list)):
	if i % 2:
		even_i.append(test_list[i])
	else :
		odd_i.append(test_list[i])

res = odd_i + even_i

# print result
print("Seprated odd and even index list: " + str(res))
