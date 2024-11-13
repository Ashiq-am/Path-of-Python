# Python3 code to demonstrate working of
# Replace Elements greater than K
# Using loop

# initializing list
test_list = [3, 4, 7, 5, 6, 7, 3, 4, 6, 9]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 5

# initializing repl_chr
repl_chr = "NA"

res = []
for ele in test_list:

    # replace if greater than K
    if ele > K:
        res.append(repl_chr)
    else:
        res.append(ele)

# printing result
print("The replaced list : " + str(res))
