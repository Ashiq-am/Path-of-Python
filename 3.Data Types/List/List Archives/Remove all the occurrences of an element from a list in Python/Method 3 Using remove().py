# Python 3 code to demonstrate
# the removal of all occurrences of
# a given item using remove()

def remove_items(test_list, item):
    # remove the item for all its occurrences
    for i in test_list:
        if (i == item):
            test_list.remove(i)

    return test_list


# driver code
if __name__ == "__main__":
    # initializing the list
    test_list = [1, 3, 4, 6, 5, 1]

    # the item which is to be removed
    item = 1

    # printing the original list
    print("The original list is : " + str(test_list))

    # calling the function remove_items()
    res = remove_items(test_list, item)

    # printing result
    print("The list after performing the remove operation is : " + str(res))
