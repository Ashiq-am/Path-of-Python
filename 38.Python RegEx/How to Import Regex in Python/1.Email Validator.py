#importing the regex module
import re

#defining the function
def emailValidator(s):
  #creating the patter
  pattern = re.compile(r'\w+@\w+\.\w+')
  #matching the patter
  if pattern.match(s) :
      return True
  return False

#input email pattern : exammple@email.com'
s = "geeksforgeeks@gmail.com"
if emailValidator(s):
    print("Valid Email")
else:
    print("Invalid Email")
