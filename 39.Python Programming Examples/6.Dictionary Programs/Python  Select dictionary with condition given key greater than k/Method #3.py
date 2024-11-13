# Python3 code to demonstrate
# filtering of list of dictionary
# on basis of condition

# initialising list of dictionary
ini_list = [{'a': 1, 'b': 3, 'c': 7}, {'a': 3, 'b': 8, 'c': 17},
            {'a': 78, 'b': 12, 'c': 13}, {'a': 2, 'b': 2, 'c': 10}]

# printing initial list of dictionary
print("initial_list", str(ini_list))

# code to filter list
# where c is more than 10

res = [{k: v for (k, v) in i.items()}
       for i in ini_list if i.get('c') > 10]

# printing result
print("resultant_list", str(res))
