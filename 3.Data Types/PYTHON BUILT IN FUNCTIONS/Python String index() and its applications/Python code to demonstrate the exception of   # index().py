# Python code to demonstrate the exception of
# index()

# initializing target string
ch = "geeksforgeeks"

# initializing argument string
ch1 = "gfg"

# using index() to find position of "gfg"
# raises error
pos = ch.index(ch1)

print ("The first position of gfg is : ",end="")
print (pos)
