L = [1, 2, 3, 4, 2, 4, 1, 2]
from collections import defaultdict
# Helper Function
def ltd(l):
    """Convert list to DefaultDict"""
    d = defaultdict(int)
    for i in l:
        d[i] += 1
        return d
print(ltd(L))
