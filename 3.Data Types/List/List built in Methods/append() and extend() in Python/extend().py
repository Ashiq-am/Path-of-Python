my_list = ['geeks', 'for']
another_list = [6, 0, 4, 1]
my_list.extend(another_list)
print(my_list)















'''NOTE: A string is an iterable, so if you extend a list with a string, you’ll append 
         each character as you iterate over the string.'''












my_list = ['geeks', 'for', 6, 0, 4, 1]
my_list.extend('geeks')
print(my_list)

