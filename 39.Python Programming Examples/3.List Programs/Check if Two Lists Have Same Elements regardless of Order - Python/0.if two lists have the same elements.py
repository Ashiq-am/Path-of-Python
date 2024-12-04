def check_lists(a, b):
    # Sort both lists
    a.sort()
    b.sort()

    # Compare if sorted lists are the same
    return a == b


a = [3, 1, 2]
b = [2, 1, 3]

print(check_lists(a, b))