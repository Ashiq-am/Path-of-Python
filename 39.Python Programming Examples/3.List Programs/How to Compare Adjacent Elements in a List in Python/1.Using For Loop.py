# function for comparision
def compare(my_list):
    for i in range(len(my_list) - 1):
        # comparision between adjacant elements
        print(my_list[i], my_list[i + 1], " ", my_list[i] == my_list[i + 1])


# number list
compare([1, 2, 2, 3, 4, 4, 5])
