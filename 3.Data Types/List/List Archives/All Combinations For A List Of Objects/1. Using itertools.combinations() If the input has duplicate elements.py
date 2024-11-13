# code
from itertools import combinations

# m = list of objects.
# 1st and 3rd elements are same.
# same method can be applied
# for list of integers.
m = ['GFG', 'GeeksforGeeks', 'GFG']

# output : list of combinations.
for i in range(len(m)):
    print(list(combinations(m, i+1)))
