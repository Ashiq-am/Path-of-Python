# Python3 program Split camel case
# string to individual strings
import re


def camel_case_split(str):
    return re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', str)


# Driver code
str = "GeeksForGeeks"
print(camel_case_split(str))
