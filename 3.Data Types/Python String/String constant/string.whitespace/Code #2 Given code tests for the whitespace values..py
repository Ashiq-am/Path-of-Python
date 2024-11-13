# import string library function
import string

# An input string.
Sentence = "Hey, Geeks !, How are you?"

for i in Sentence:

    # checking whether the whitespace is present
    if i in string.whitespace:
        # Printing the whitespace values
        print("printable Value is: " + i)
