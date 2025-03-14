# importing the module
import re

# opening and reading the file
with open('C:/Users/user/Desktop/New Text Document.txt') as fh:
    fstring = fh.readlines()

# decalring the regex pattern for IP addresses
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

# initializing the list object
lst=[]

# extracting the IP addresses
for line in fstring:
    lst.append(pattern.search(line)[0])

# displaying the extracted IP adresses
print(lst)
