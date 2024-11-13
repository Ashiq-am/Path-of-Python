# WRITING OPERATIONS
# creates a file named emails.txt
fhand = open("emails.txt", "w")

# this enters the values into the file
fhand.write('''stephen.marquard@uct.ac.za
stephen.marquard@uct.ac.za
louis@media.berkeley.edu
louis@media.berkeley.edu
louis@media.berkeley.edu
louis@media.berkeley.edu
ray@media.berkeley.edu
ray@media.berkeley.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu''')

# closing the file
fhand.close()
