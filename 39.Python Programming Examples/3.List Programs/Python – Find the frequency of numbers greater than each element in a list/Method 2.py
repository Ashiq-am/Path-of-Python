# import module
import bisect

# initializing list
test_list = [6, 3, 7, 1, 2, 4]

# printing original list
print("The original list is : " + str(test_list))

# sorting before bisect
temp = sorted(test_list)

# getting total greater elements for each element
res = [len(test_list) - bisect.bisect_left(temp, ele) for ele in test_list]

# printing result
print("Greater elements Frequency list : " + str(res))
