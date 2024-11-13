# initializing list
test_list = [345, 893, 1948, 34, 2346]

# printing original list
print("The original list is : " + str(test_list))

odd_sum = 0
even_sum = 0

for sub in test_list:
    for ele in str(sub):

        # adding in particular summation according to value
        if int(ele) % 2 == 0:
            even_sum += int(ele)
        else:
            odd_sum += int(ele)

# printing result
print("Odd digit sum : " + str(odd_sum))
print("Even digit sum : " + str(even_sum))
