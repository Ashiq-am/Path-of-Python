def count_occur(list1):
    for i in range(0, len(l1)):
        a = 0
        row = []
        if i not in l:
            for j in range(0, len(l1)):

                # matching items from both lists
                if l1[i] == l1[j]:
                    # on match counter increments by 1
                    a = a + 1

            row.append(l1[i])
            row.append(a)

            # append function will append
            # 1d list items to 2d list
            l.append(row)

    # below code is to eliminate
    # repetitive list items
    for j in l:
        if j not in unq_l:
            unq_l.append(j)

    return unq_l


# Driver code
l1 = [3, 5, 7, 2, 3, 5, 9.1]
l = []
unq_l = []

print(count_occur(l1))
