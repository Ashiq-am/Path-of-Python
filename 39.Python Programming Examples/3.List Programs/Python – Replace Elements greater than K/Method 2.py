# Python3 code to demonstrate working of
# Replace Elements greater than K
# Using list comprehension

# initializing list
test_list = [3, 4, 7, 5, 6, 7, 3, 4, 6, 9]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 5

# initializing repl_chr
repl_chr = "NA"

# one liner to solve problem
res = [repl_chr if ele > K else ele for ele in test_list]

# printing result
print("The replaced list : " + str(res))
