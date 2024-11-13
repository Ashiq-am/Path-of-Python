# create a list of subjects
data = ["java", "python", "HTML", "PHP"]

print("Indices in list:")

# get the indices using list comphrension method
print([i for i in range(len(data))])

print("values in list:")

# get the values from indices using list
# comphrension method
print([data[i] for i in range(len(data))])
