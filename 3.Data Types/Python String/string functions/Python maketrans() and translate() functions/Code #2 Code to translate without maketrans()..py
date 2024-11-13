# Python3 code to demostrate
# translations without
# maketrans()

# specifying the mapping
# using ASCII
table = { 119 : 103, 121 : 102, 117 : None }

# target string
trg = "weeksyourweeks"

# Printing original string
print ("The string before translating is : ", end ="")
print (trg)

# using translate() to make translations.
print ("The string after translating is : ", end ="")
print (trg.translate(table))
