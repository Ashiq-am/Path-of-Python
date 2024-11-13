def convert_heap(list_li):
    # list to hold salary values
    sal_li = []

    # extrat salary values
    for i in range(0, len(list_li)):
        sal_li.append(list_li[i][1]['Salary'])

    print("Before heapify :", sal_li, "\n")

    # heapify the salary values
    hq.heapify(sal_li)

    print("After salary :", sal_li, "\n")

    # list to hold the final dictionary as heap
    final = []

    # reconstruction of dictionary as heap
    # yields a list of tuples of key-value pairs
    for i in range(0, len(sal_li)):

        for j in range(0, len(sal_li)):

            if list_li[j][1]['Salary'] == sal_li[i]:
                final.append(list_li[j])

            # list of tuples to dictionary
    final = dict(final)

    return final
