my_file = open("geeksforgeeks.txt","a")
my_file.write("..>>Visit geeksforgeeks.org for more!!<<..")
my_file.close()

# reading the file
my_file = open("geeksforgeeks.txt","r")
print(my_file.read())
