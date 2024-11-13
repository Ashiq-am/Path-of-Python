# Python3 code to remove whitespace
import re


def remove(string):
    pattern = re.compile(r'\s+')
    return re.sub(pattern, '', string)


# Driver Program
string = ' g e e k '
print(remove(string))
