# Python3 code to demonstrate working of
# Sort String by Custom Substrings
# Using sorted() + comparator + regex()
import re


# helper function to solve problem
def hlper_fnc(ele):
    temp = re.search("(\d+)$", ele).group()
    return temp_dict[temp] if temp in temp_dict else int(temp)


# initializing list
test_list = ["Good at 4", "Wake at 7", "Work till 6", "Sleep at 11"]

# printing original list
print("The original list : " + str(test_list))

# initializing subtring list
subord_list = ["6", "7", "4", "11"]

# crearing inverse mapping with index
temp_dict = {val: key for key, val in enumerate(test_list)}

# sorting using comparator
test_list.sort(key=lambda ele: hlper_fnc(ele))

# printing result
print("The sorted list : " + str(test_list))
