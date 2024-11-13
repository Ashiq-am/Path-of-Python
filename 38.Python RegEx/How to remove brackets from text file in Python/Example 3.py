# importing re module for creating
# regex expression
import re

# reading line by line
with open('input.txt', 'r') as f:
    # store in text variable
    text = f.read()

    # getting the pattern for [],(),{}
    # brackets and replace them to empty string
    # creating the regex pattern & use re.sub()
    pattern = re.sub(r"[\([{})\]]", "", text)

# Appending the changes in new file
# It will create new file in the directory
# and write the changes in the file.
with open('output.txt', 'w') as my_file:
    my_file.write(pattern)
