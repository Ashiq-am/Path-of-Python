import re

string = "1,2,3,4,5"
pattern = ","
numbers = re.split(pattern, string)
print(numbers)
