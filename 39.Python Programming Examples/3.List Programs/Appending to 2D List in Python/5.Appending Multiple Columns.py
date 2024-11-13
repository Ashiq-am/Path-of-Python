#defining our append function
def appendList(l, element):
    for i in range(len(l)):
        for ele in element:
            l[i].append(ele[i])
    return l

#defining a 2D list
myList = [[1,2,3], [4,5,6], [7,8,9]]

#new element
newList = [[10,11,12], [13,14,15], [16,17,18]]

#function calling
myList = appendList(myList, newList)
print(myList)
