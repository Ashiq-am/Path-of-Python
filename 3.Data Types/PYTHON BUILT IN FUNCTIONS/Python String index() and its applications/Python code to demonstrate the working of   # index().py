# Python code to demonstrate the working of
# index()

# initializing target string
ch = "geeksforgeeks"

# initializing argument string
ch1 = "geeks"

# using index() to find position of "geeks"
# starting from 2nd index
# prints 8
pos = ch.index(ch1,2)

print ("The first position of geeks after 2nd index : ",end="")
print (pos)
