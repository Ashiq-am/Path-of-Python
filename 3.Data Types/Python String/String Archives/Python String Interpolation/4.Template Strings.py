# Python program to demonstrate
# string interpolation


from string import Template

n1 = 'Hello'
n2 ='GeeksforGeeks'

# made a template which we used to
# pass two variable so n3 and n4
# formal and n1 and n2 actual
n = Template('$n3 ! This is $n4.')

# and pass the parameters into the template string.
print(n.substitute(n3 = n1, n4 = n2))
