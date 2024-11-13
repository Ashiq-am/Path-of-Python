#defining our append function
def appendList(l,element):
    l.append(element)
    return l

#defining a 2D list
myList = [[1,2,3], [4,5,6]]

#new element
newList = [[7,8,9],[10,11,12]]

#function calling
myList = appendList(myList,newList)
print(myList)
