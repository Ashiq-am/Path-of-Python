# importing module
import pyminizip

# input file path
inpt = "./Text.txt"

# prefix path
pre = None

# output zip file path
oupt = "./output.zip"

# set password value
password = "GFG"

# compress level
com_lvl = 5

# compressing file
pyminizip.compress(inpt, None, oupt, password, com_lvl)
