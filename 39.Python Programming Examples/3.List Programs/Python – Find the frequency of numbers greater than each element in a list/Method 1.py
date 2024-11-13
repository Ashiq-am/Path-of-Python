# initializing list
test_list = [6, 3, 7, 1, 2, 4]

# printing original list
print("The original list is : " + str(test_list))

# sum() performs counts of element which are Greater or equal to
res = [sum(1 for ele in test_list if sub <= ele) for sub in test_list]

# printing result
print("Greater elements Frequency list : " + str(res))
