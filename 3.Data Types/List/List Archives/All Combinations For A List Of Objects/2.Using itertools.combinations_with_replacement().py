# code
from itertools import combinations_with_replacement

# m = list of objects.
# same method can be applied
# for list of integers.
m = ['GFG', 'GeeksforGeeks', 'Geeks']

# output : list of combinations.
for i in range(len(m)):
    print(list(combinations_with_replacement(m, i+1)))
