''''''


'''Code#1'''



# Python3 program for illustration
# of values() method of dictionary


# numerical values
dictionary = {"raj": 2, "striver": 3, "vikram": 4}
print(dictionary.values())


# string values
dictionary = {"geeks": "5", "for": "3", "Geeks": "5"}
print(dictionary.values())









"""Practical Application:
Given name and salary, return the total salary of all employees."""







'''Code#2'''



# Python3 program for illustration
# of values() method in finding total salary


# stores name and corresponding salaries
salary = {"raj" : 50000, "striver" : 60000, "vikram" : 5000}

# stores the salaries only
list1 = salary.values()
print(sum(list1)) # prints the sum of all salaries
