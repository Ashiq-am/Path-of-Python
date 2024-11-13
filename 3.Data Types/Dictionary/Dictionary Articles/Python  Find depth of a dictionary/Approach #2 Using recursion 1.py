# Python3 Program to find depth of a dictionary
def dict_depth(my_dict):
    if isinstance(my_dict, dict):
        return 1 + (max(map(dict_depth, my_dict.values()))
                    if my_dict else 0)

    return 0


# Driver code
my_dict = {1: 'a', 2: {3: {4: {}}}}
print(dict_depth(my_dict))
