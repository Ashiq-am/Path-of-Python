# Python3 code to demonstrate working of
# Time Strings to Seconds in Tuple List
# Using loop + split()

# initializing list
test_list = [("5:12", "9:45"), ("12:34", "4:50"), ("10:40",)]

# printing original list
print("The original list is : " + str(test_list))

res = []
for sub in test_list:
    tup = tuple()

    # iterating each tuple
    for ele in sub:
        # perform conversion
        min, sec = ele.split(":")
        secs = 60 * int(min) + int(sec)
        tup += (secs,)
    res.append(tup)

# printing result
print("The corresponding seconds : " + str(res))
