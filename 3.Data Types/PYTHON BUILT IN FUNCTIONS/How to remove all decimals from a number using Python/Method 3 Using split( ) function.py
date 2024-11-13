value1 = [998.99, 56.8, 25.6, -52.0]

# values are split at decimal point
lst = []
for each in value1:
	lst.append(str(each).split('.')[0])

# all values converting to integer data type
final_list = [int(i) for i in lst]
print(final_list)
