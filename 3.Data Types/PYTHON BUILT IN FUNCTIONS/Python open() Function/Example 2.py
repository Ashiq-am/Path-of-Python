my_file = open("geeksforgeeks.txt", "w")
my_file.write("Geeksforgeeks is best for DSA")
my_file.close()

#let's read the contents of the file now
my_file = open("geeksforgeeks.txt","r")
print(my_file.read())
