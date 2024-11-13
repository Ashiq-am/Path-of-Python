# Python code to demonstrate
# to find nth occurrence of substring

# Initialising values
ini_str = "abababababab"
substr = "ab"
occurrence = 4

# Finding nth occurrence of substring
inilist = [i for i in range(0, len(ini_str))
           if ini_str[i:].startswith(substr)]

if len(inilist) >= 4:

    # Printing result
    print("Nth occurrence of substring at", inilist[occurrence - 1])
else:
    print("No {} occurrence of substring lies in given string".format(occurrence))

