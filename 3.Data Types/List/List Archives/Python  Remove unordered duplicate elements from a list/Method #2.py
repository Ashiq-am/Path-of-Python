# Python code to remove duplicate
# unordered elements from a list
# List initialisation
Input = ['gfg', 'ggf', 'fgg', 'for', 'orf',
				'ofr', 'rfo', 'rof', 'fro']

# Getting unique nos
Output = list({''.join(sorted(n)) for n in Input})

# Printing Output
print(Output)
