# Python3 code to convert tuple
# into string
def count(listOfTuple):
    count_map = {}
    for i in listOfTuple:
        count_map[i] = count_map.get(i, 0) + 1
    print(count_map)


# Driver code
print("Test Case 1:")
listOfTuple = [('a', 'e'), ('b', 'x'), ('b', 'x'),
               ('a', 'e'), ('b', 'x')]

count(listOfTuple)
