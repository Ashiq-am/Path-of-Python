# Python code to sort list of percentage

# List initialization
Input =['2.5 %', '6.4 %', '91.6 %', '11.5 %']

# removing % and converting to float
# then apply sort function
Input.sort(key = lambda x: float(x[:-1]))

# printing output
print(Input)
