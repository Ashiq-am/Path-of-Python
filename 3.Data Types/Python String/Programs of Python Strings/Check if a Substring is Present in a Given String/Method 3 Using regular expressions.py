# When you have imported the re module, you can start using regular expressions.
import re

# Take input from users
MyString1 = "A geek in need is a geek indeed"
MyString2 ="geek"

# re.search() returns a Match object if there is a match anywhere in the string
if re.search( MyString2, MyString1 ):
	print("YES,string '{0}' is present in string '{1}' " .format(MyString2,MyString1))
else:
	print("NO,string '{0}' is not present in string {1} " .format(MyString2, MyString1) )
