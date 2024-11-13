#defining our append function
def appendList(l,element):
    for i in range(len(element)):
        l[i].append(element[i])
    return l

#defining a 2D list
myList = [[1,2,3], [4,5,6], [7,8,9]]

#new element
newList = [10,11,12]

#function calling
myList = appendList(myList,newList)
print(myList)
