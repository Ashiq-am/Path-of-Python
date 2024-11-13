# Declaring arrays using list in Python
array = [12, 34, 45, 32, 54]

for i in range(0, len(array)):
    print(array[i], end=" ")

# Inserting element in array
array.append(99);

# Modifying element in an array
array[0] = 100;

print("\nArray after modification :")

for i in range(0, len(array)):
    print(array[i], end=" ")
