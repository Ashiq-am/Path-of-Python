def contains_even_number(l):
    n = len(l)
    i = 0
    while i < n:
        if l[i] % 2 == 0:
            print("list contains an even number")
            break
        i += 1

    # This else executes only if break is NEVER
    # reached and loop terminated after all
    # iterations
    else:
        print("list does not contain an even number")


# Driver code
print("For List 1:")
contains_even_number([1, 9, 8])
print(" \nFor List 2:")
contains_even_number([1, 3, 5])
