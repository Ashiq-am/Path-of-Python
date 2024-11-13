# Using while loop

lis = [1, 2, 3, 4, 5]
i = 0

while (i < len(lis)):
    print(lis[i], end=" ")

    # Changing the value of
    # i inside the loop will
    # change it's value at the
    # time of checking condition
    i += 2

