import re


regex = re.compile(r'([\d]{2})-([\d]{2})-([\d]{4})')

# search method
print('compiled reg expr', regex.search('26-08-2020'))

# sub method
print(regex.sub(r'\1.\2.\3', '26-08-2020'))
