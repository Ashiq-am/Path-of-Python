import heapq as hq


def get_list(d):
    list_li = list(d.items())

    print("Dictionary as list", list_li, "\n")

    return (list_li)


def convert_heap(list_li):
    # list to hold salary values
    sal_li = []

    # extrat salary values
    for i in range(0, len(list_li)):
        sal_li.append(list_li[i][1]['Salary'])

    print("Before heapify :", sal_li, "\n")

    # heapify the salary values
    hq.heapify(sal_li)

    print("After heapify :", sal_li, "\n")

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


nested_dict = {
    "emp01": {
        "name": "Kate",
        "age": 22,
        "designation": "Analyst",
        "Salary": 30000
    },
    "emp02": {
        "name": "Rina",
        "age": 20,
        "designation": "Programmer",
        "Salary": 25000
    },
    "emp03": {
        "name": "Vikas",
        "age": 42,
        "designation": "Manager",
        "Salary": 35000
    },
    "emp04": {
        "name": "manish",
        "age": 42,
        "designation": "Manager",
        "Salary": 15000
    }
}

list_li = get_list(nested_dict)

final = convert_heap(list_li)

print("Dictionary as heap :", final)
