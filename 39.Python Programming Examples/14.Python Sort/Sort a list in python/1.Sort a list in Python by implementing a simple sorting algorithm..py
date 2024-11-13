# Sample list
my_list = [64, 34, 25, 12, 22, 11, 90]

# Bubble sort algorithm
n = len(my_list)
for i in range(n):
    for j in range(0, n-i-1):
        if my_list[j] > my_list[j+1]:
            # Swap if the element found is greater
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

# Print the sorted list
print(my_list)
