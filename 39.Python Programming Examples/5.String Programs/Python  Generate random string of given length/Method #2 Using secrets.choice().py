# Python3 code to demonstrate
# generating random strings
# using secrets.choice()
import secrets
import string

# initializing size of string
N = 7

# using random.choices()
# generating random strings
res = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
												for i in range(N))

# print result
print("The generated random string : " + str(res))
