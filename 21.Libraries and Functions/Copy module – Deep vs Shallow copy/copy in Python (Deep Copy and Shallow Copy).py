''''''



"""In order to make these copy, we use copy module.
 We use copy module for shallow and deep copy operations. For Example"""




# importing copy module
import copy

# initializing list 1
li1 = [1, 2, [3,5], 4]


# using copy for shallow copy
li2 = copy.copy(li1)

# using deepcopy for deepcopy
li3 = copy.deepcopy(li1)






'''In the above code, the copy() returns a shallow copy of list and deepcopy() return a deep copy of list.'''