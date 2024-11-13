def find_divisibles(myList, num):
    # list comprehension to check if the number is divisible
    return [i for i in myList if i % num == 0]

myList = [8, 14, 21, 36, 43, 57, 63, 71, 83, 93]
num = 3
print(find_divisibles(myList, num))
