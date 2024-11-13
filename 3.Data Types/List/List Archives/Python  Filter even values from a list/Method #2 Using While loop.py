# Python code to filter even values from a list

# Initialisation of list
lis = [1, 2, 3, 4, 5]
num = 0

# Output list initialisation
out = []
while (num < len(lis)):

    # checking condition
    if lis[num] % 2 == 0:
        out.append(lis[num])
    # increment num
    num += 1

# printing output
print(out)
