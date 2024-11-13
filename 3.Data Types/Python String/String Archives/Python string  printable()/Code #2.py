# import string library function
import string

# An input string.
Sentence = "Hey, Geeks !, How are you?"

for i in Sentence:

    # checking whether the char is printable value
    if i in string.printable:
        # Printing the printable values
        print("printable Value is: " + i)
