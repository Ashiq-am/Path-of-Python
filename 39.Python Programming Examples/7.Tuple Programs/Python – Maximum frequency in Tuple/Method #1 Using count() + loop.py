# Python3 code to demonstrate working of
# Maximum frequency in Tuple
# Using loop + count()

# initializing tuple
test_tuple = (6, 7, 8, 6, 7, 10)

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Maximum frequency in Tuple
# Using loop + count()
cnt = 0
res = test_tuple[0]
for ele in test_tuple:
    curr_freq = test_tuple.count(ele)
    if (curr_freq > cnt):
        cnt = curr_freq
        res = ele

    # printing result
print("Maximum element frequency tuple : " + str(res))
