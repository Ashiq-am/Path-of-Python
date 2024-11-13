# Python3 code to convert tuple
# into string
def count(listOfTuple):
    flag = False

    # To append Duplicate elements in list
    coll_list = []
    coll_cnt = 0
    for t in listOfTuple:

        # To check if Duplicate exist
        if t in coll_list:
            flag = True
            continue

        else:
            coll_cnt = 0
            for b in listOfTuple:
                if b[0] == t[0] and b[1] == t[1]:
                    coll_cnt = coll_cnt + 1

            # To print count if Duplicate of element exist
            if (coll_cnt > 1):
                print(t, "-", coll_cnt)
            coll_list.append(t)

    if flag == False:
        print("No Duplicates")

    # Driver code


print("Test Case 1:")
listOfTuple = [('a', 'e'), ('b', 'x'), ('b', 'x'),
               ('a', 'e'), ('b', 'x')]

count(listOfTuple)

print("Test Case 2:")
listOfTuple = [(0, 5), (6, 9), (0, 8)]
count(listOfTuple)
