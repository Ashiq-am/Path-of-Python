# Python code to demonstrate
# to split strings
# on uppercase letter

# Initialising string
ini_str = 'GeeksForGeeks'

# Printing Initial string
print ("Initial String", ini_str)

# Splitting on UpperCase
res_pos = [i for i, e in enumerate(ini_str+'A') if e.isupper()]
res_list = [ini_str[res_pos[j]:res_pos[j + 1]]
			for j in range(len(res_pos)-1)]

# Printing result
print("Resultant prefix", str(res_list))
