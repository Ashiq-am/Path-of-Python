# create a index list that stores list
indexlist = [0, 1, 2, 3]

# create a list of subjects
data = ["java", "python", "HTML", "PHP"]


print("index and values in list:")

# get the values from indices using zip method
for index, value in zip(indexlist, data):
	print(index, value)
