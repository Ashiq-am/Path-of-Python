#importing the regex module
import re as regex

#defining the function
def phoneValidator(s):
  #creating the patter
  pattern = regex.compile(r'\d{3}-\d{3}-\d{4}$')
  #matching the patter
  if pattern.match(s) :
      return True
  return False


#phone number should be in this pattern : 111-111-1111
s = "987-654-3210"
if phoneValidator(s):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")
