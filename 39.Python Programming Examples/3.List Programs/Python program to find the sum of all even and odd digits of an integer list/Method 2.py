# initializing list
test_list = [345, 893, 1948, 34, 2346]

# printing original list
print("The original list is : " + str(test_list))

odd_sum = 0
even_sum = 0

for sub in test_list:
    # sum() used to get summation of even and odd elements
    odd_sum += sum([int(ele) for ele in str(sub) if int(ele) % 2 == 1])
    even_sum += sum([int(ele) for ele in str(sub) if int(ele) % 2 == 0])

# printing result
print("Odd digit sum : " + str(odd_sum))
print("Even digit sum : " + str(even_sum))
