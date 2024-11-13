# Program without using any external library
s = "Python is great and Java is also great"
l = s.split()
k = []
for i in l:

	# If condition is used to store unique string
	# in another list 'k'
	if (s.count(i)>1 and (i not in k)or s.count(i)==1):
		k.append(i)
print(' '.join(k))
