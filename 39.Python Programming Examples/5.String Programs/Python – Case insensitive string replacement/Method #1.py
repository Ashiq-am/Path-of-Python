# Python3 code to demonstrate working of
# Case insensitive Replace
# Using re.IGNORECASE + re.escape() + re.sub()
import re

# initializing string
test_str = "gfg is BeSt"

# printing original string
print("The original string is : " + str(test_str))

# initializing replace string
repl = "good"

# initializing substring to be replaced
subs = "best"

# re.IGNORECASE ignoring cases
# compilation step to escape the word for all cases
compiled = re.compile(re.escape(subs), re.IGNORECASE)
res = compiled.sub(repl, test_str)

# printing result
print("Replaced String : " + str(res))
