#defining our append function
def appendList(l, element, pos):
    for i in range(len(l)):
        l[i].insert(pos, element[i])
    return l

#defining a 2D list
myList = [[1,2,3], [4,5,6], [7,8,9]]

#new element
newList = [10,11,12]

# define position
pos = 1

#function calling
myList = appendList(myList, newList, pos)
print(myList)
