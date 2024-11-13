from itertools import groupby

original_list = [1, 1, 2, 3, 3, 3, 4, 5, 5]
split_list = [list(group) for key, group in groupby(original_list)]
print(split_list)
