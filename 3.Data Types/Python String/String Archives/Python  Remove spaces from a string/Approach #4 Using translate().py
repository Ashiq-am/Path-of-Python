# Python code to remove whitespace
import string


def remove(string):
    return string.translate(None, ' \n\t\r')


# Driver Program
string = ' g e e k '
print(remove(string))
