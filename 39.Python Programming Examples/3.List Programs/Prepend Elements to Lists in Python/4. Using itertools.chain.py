import itertools

my_list = [2, 3, 4]
my_list = list(itertools.chain([1], my_list))
print(my_list)
