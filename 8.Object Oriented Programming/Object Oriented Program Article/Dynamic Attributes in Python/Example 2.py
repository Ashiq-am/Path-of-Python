class GFG:
    employee = True


# Driver Code
e1 = GFG()
e2 = GFG()

e1.employee = False
e2.name = "Nikhil"

print(e1.employee)
print(e2.employee)
print(e2.name)

# this will raise an error
# as name is a dynamic attribute
# created only for the e2 object
print(e1.name)
