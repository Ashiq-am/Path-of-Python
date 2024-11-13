import random

arr=[1,2,3,4,5,6]
n=len(arr)-1
for i in range(n):
	random_index = random.randint(0, n)
	temp = arr.pop(random_index)
	arr.append(temp)
print(arr)
