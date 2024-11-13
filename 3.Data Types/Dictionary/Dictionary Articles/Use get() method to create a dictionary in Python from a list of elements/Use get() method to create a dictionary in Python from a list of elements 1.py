li =['a', 'b', 'c', 'a', 'd', 'e', 'b', 'a']
di ={}

for ele in li:
	di[ele]= di.get(ele, 0)+1

print(di)
