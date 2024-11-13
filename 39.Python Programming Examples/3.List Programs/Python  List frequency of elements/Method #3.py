d = {}

test_list = [[3, 5, 4],
			[6, 2, 4],
			[1, 3, 6]]

for x in test_list:

    for i in x:
        d[i] = d.get(i,0) + 1

# Orignal list
print(f"The original list : {test_list}" )

# printing result
print(f"The list frequency of elements is : {d}" )
