import heapq as hq


def heapify_dict(d):
    # convert to list of tuples
    li = list(dict1.items())

    hq.heapify(li)

    li = dict(li)

    print("Dictionary as heap :", li)


dict1 = {11: 121, 2: 4, 5: 25, 3: 9}

print("Before adding new values")
heapify_dict(dict1)

# add new values to dictionary
dict1[4] = 16
dict1[1] = 1

print("Updated dictionary :", dict1)

print("After adding new values")
heapify_dict(dict1)
