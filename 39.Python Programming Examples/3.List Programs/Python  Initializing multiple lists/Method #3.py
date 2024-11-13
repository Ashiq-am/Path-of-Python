# Python3 code to demonstrate
# to initialize multiple lists
# using defaultdict()
import collections

# using defaultdict()
# to initialize multiple lists
# no need to initialize with empty lists
mul_list_dict = collections.defaultdict(list)
mul_list_dict['list1'].append(1)
mul_list_dict['list2'].append(2)
mul_list_dict['list3'].append(3)
mul_list_dict['list4'].append(4)

# printing lists
print ("The initialized lists are : ")
print ("List 1 : " + str(mul_list_dict['list1']))
print ("List 2 : " + str(mul_list_dict['list2']))
print ("List 3 : " + str(mul_list_dict['list3']))
print ("List 4 : " + str(mul_list_dict['list4']))
