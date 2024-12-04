from collections import Counter

def check_lists(a, b):
    # Use Counter to count elements in both lists
    return Counter(a) == Counter(b)

a = [3, 1, 2]
b = [2, 1, 3]

print(check_lists(a, b))