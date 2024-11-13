import math
import string
import sys


# reading the text file
# This functio will return a
# list of the lines of text
# in the file.
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            data = f.read()
        return data

    except IOError:
        print("Error opening or reading input file: ", filename)
        sys.exit()


# splitting the text lines into words
# translation table is a global variable
# mapping upper case to lower case and
# punctuation to spaces
translation_table = str.maketrans(string.punctuation + string.ascii_uppercase,
                                  " " * len(string.punctuation) + string.ascii_lowercase)


# returns a list of the words
# in the file
def get_words_from_line_list(text):
    text = text.translate(translation_table)
    word_list = text.split()

    return word_list
