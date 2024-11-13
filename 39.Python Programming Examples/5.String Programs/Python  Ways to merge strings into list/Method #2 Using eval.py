# Python code to merge all strings into a single list.

# Initialization of strings
str1 ="['Geeks', 'for', 'Geeks']"
str2 ="['paras.j', 'jain.l']"
str3 ="['india']"


out = [str1, str2, str3]

out = eval('+'.join(out))

# printing output
print(out)
