# Python3 program to demonstrate global() function

# global variable
name = 'gautam'

print('Before modification:', name)

# Calling global()
globals()['name'] = 'gautam karakoti'
print('After modification:', name)
