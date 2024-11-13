# function for comparision
def compare(my_list):
    # comparision between adjuscant elements
    newList = [[my_list[i], my_list[i + 1], my_list[i] == my_list[i + 1]]
               for i in range(len(my_list) - 1)]
    for i in newList:
        print(i[0], i[1], " ", i[2])


# string list
compare(['GFG', 'gfg', 'Coding', 'Apple', 'Python', 'Python'])
