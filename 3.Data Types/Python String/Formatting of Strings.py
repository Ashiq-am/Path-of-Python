'''Strings in Python can be formatted with the use of format() method which is very versatile and powerful
tool for formatting of Strings.

Format method in String contains curly braces {}
as placeholders which can hold arguments according to position or keyword to specify the order.'''




# Python Program for
# Formatting of Strings

# Default order
String1 = "{} {} {}".format('Geeks', 'For', 'Life')
print("Print String in default order: ")
print(String1)

# Positional Formatting
String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life')
print("\nPrint String in Positional order: ")
print(String1)

# Keyword Formatting
String1 = "{l} {f} {g}".format(g = 'Geeks', f = 'For', l = 'Life')
print("\nPrint String in order of Keywords: ")
print(String1)










'''Integers such as Binary, hexadecimal, etc. and floats can be rounded or displayed in the exponent 
form with the use of format specifiers.

'''




# Formatting of Integers
String1 = "{0:b}".format(16)
print("\nBinary representation of 16 is ")
print(String1)

# Formatting of Floats
String1 = "{0:e}".format(165.6458)
print("\nExponent representation of 165.6458 is ")
print(String1)

# Rounding off Integers
String1 = "{0:.2f}".format(1/6)
print("\none-sixth is : ")
print(String1)












'''A string can be left() or center(^) justified with the use of format specifiers, separated by colon(:).'''


# String alignment
String1 = "|{:<10}|{:^10}|{:>10}|".format('Geeks','for','Geeks')
print("\nLeft, center and right alignment with Formatting: ")
print(String1)

# To demonstrate aligning of spaces
String1 = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 2009)
print(String1)









"""Old style formatting was done without the use of format method by using % operator"""



# Python Program for
# Old Style Formatting
# of Integers

Integer1 = 12.3456789
print("Formatting in 3.2f format: ")
print('The value of Integer1 is %3.2f' %Integer1)
print("\nFormatting in 3.4f format: ")
print('The value of Integer1 is %3.4f' %Integer1)
