# Define function using lambda for cube root
cube_root= lambda x: x**(1/3)

# Call the lambda function
print(cube_root(27))


languages = ['Sanskrut', 'English', 'French', 'German']


# Define function using lambda
l_check_language = lambda x: True if x in languages else False

# Call the lambda function
print(l_check_language('Sanskrut'))
