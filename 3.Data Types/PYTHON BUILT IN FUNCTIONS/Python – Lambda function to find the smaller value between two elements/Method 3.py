# Two lambda functions will be stored
# in tuple such that 1st element is b
# and 2nd element will be b.
# if [a<b] is true it return 1 and
# element with index 1 will print
# else if [a<b] is false it return 0,
# so element with index 0 will print
a = 5
b = 8
print((lambda: b, lambda: a)[a < b]())
