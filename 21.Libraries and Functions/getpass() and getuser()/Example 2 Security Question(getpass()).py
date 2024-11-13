''''''



'''There are certain programs that ask for security questions rather than asking for passwords for better security. 
Here, the prompt can be changed to any value.'''





# A simple Python program to demonstrate
# getpass.getpass() to read security question
import getpass

p = getpass.getpass(prompt='Your favorite flower? ')

if p.lower() == 'rose':
	print('Welcome..!!!')
else:
	print('The answer entered by you is incorrect..!!!')







