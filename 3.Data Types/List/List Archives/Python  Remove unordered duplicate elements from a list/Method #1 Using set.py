# Python code to remove duplicate
# unordered elements from a list
from collections import Counter

# List initialisation
Input = ['1213', '1231', '1123', '1132', '2113',
         '2311', '0007', '0016', '0025', '0034',
         '0043', '0052', '0061', '0070', '0304',
         '0313', '0322', '0098', '9800', '0331',
         '0340', '0403', '0412', '0421', '0430',
         '0502', '8900', '8009', '0511', '0520',
         '0601', '0610', '0700', '1006', '1015']

# Set initialisation
s = set()

# Output list initialisation
output = []

for i in Input:
    if tuple(Counter(sorted(i, key=int)).items()) in s:
        pass

    else:
        s.add(tuple(Counter(sorted(i, key=int)).items()))
        output.append(i)

    # Printing output
print(output)
