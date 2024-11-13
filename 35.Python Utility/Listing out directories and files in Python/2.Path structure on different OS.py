# Python version : 2.7.12

# len()
# To count number of items in a list
# To count number of characters in a string
evens = [ 2, 34, 6, 8, 10]
print(len(evens))

city = "Bangalore"
print(len(city), "\n")

# str() : Converting into string representation
odds = [ 1, 3, 67, 45, 83, 59]
year = 2017

print(odds)
print(str(odds) + " A list.\n")
print(year)
print(str(year) + " A year.\n")


# enumerate() : iterating over index & value of a list
for (index, item) in enumerate(odds):
	print(index, item)


# abspath() : Getting absolute path of passed argument(path)
import os
absolute_path = os.path.abspath(".")
print("\n", absolute_path, "\n")


# isdir() : To check if passed argument is valid directory path
answer = os.path.isdir("/Users/admin/Desktop/js")
print(answer)


# isfile() : To check if the passed argument is valid file path
answer = os.path.isfile("/Users/admin/Desktop/js/array.js")
print(answer, "\n")


# list() : To create list
details = { "name":"Rojert Rendrick", "age":24, "city":"Bangalore" }
keys = list( details )
print(keys, "\n")

# append() : Appending items to list
print(evens)
evens.append(98)
evens.append(64)
print(evens, "\n")

# repetition operator(*) on strings
print("Python"*3)
print("#"*20)
