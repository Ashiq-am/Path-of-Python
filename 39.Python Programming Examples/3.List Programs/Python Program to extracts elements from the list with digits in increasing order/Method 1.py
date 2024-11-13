# initializing list
test_list = [1234, 7373, 3643, 3527, 148]

# printing original list
print("The original list is : " + str(test_list))

# loop to check for each element
res = []
for ele in test_list:
    flag = True

    for idx in range(len(str(ele)) - 1):

        # checking for each next digit
        if str(ele)[idx + 1] <= str(ele)[idx]:
            flag = False

    if flag:
        res.append(ele)

# printing result
print("Extracted increasing digits : " + str(res))
