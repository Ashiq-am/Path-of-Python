# Python code to demonstrate
# application of encode-decode

# input from user
# user = raw_input()
# pass = raw_input()

user = "geeksforgeeks"
passw = "i_lv_coding"

# converting password to base64 encoding
passw = passw.encode('base64', 'strict')

# input from user
# user_login = raw_input()
# pass_login = raw_input()

user_login = "geeksforgeeks"

# wrongly entered password
pass_wrong = "geeksforgeeks"

print("Password entered : " + pass_wrong)

if(pass_wrong == passw.decode('base64', 'strict')):
    print("You are logged in !!")
else :
    print("Wrong Password !!")

print('\r')

# correctly entered password
pass_right = "i_lv_coding"

print("Password entered : " + pass_right)

if(pass_right == passw.decode('base64', 'strict')):
    print("You are logged in !!")
else :
    print("Wrong Password !!")
