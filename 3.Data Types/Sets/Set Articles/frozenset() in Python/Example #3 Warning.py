# Python program to understand
# use of frozenset function

# creating a list
favourite_subject = ["OS", "DBMS", "Algo"]

# making it frozenset type
f_subject = frozenset(favourite_subject)

# below line will generate error

f_subject[1] = "Networking"
