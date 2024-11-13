# code
from itertools import combinations

# m = list of objects.
# same method can be applied
# for list of integers.
m = ['GFG', 'GeeksforGeeks', 'Geeks']
# display
for i in range(len(m)):
    print(list(combinations(m, i+1)))
