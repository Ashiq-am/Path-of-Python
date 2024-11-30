a = [1, 2, 3]

#Using list comphrehension
#Adds [3, 4] to the end of 'a'
a += [x + 3 for x in range(2)]
print(a)