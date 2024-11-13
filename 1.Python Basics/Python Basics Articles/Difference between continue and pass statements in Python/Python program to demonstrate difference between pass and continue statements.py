# Python program to demonstrate
# difference between pass and
# continue statements

s = "geeks"

# Pass statement
for i in s:
    if i == 'k':
        print('Pass executed')
        pass
    print(i)

print()

# Continue statement
for i in s:
    if i == 'k':
        print('Continue executed')
        continue
    print(i)
