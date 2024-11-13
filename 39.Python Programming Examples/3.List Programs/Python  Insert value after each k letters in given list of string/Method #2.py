# Python program to insert value after
# each k letters in given list of string
from itertools import chain

list1 = ['p', 'y', 't', 'h', 'o', 'n']

# printing original list
print("Original list : " + str(list1))

# initializing k
k = 'x'

# initializing N
N = 3

# inserting K after every Nth number
output = list(chain(*[list1[i: i + N] + [k]
                      if len(list1[i: i + N]) == N else list1[i: i + N]
                      for i in range(0, len(list1), N)]))

# printing result
print("The lists after insertion : " + str(output))
