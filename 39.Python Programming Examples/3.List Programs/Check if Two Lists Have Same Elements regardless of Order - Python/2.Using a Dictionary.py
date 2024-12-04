def check_lists(a, b):
    # If the lengths of the lists are different, they cannot have the same elements
    if len(a) != len(b):
        return False

    # Create a dictionary to count occurrences of elements in list a
    count_a = {}
    for item in a:
        count_a[item] = count_a.get(item, 0) + 1

    # Check if the elements in list b match the counts in list a
    for item in b:
        if count_a.get(item, 0) == 0:
            return False
        count_a[item] -= 1

    return True

a = [3, 1, 2]
b = [2, 1, 3]

print(check_lists(a, b))