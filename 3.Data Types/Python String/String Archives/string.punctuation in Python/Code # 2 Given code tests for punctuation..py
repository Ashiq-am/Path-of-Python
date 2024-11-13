# import string library function
import string

# An input string.
Sentence = "Hey, Geeks !, How are you?"

for i in Sentence:

    # checking whether the char is punctuation.
    if i in string.punctuation:
        # Printing the punctuation values
        print("Punctuation: " + i)

