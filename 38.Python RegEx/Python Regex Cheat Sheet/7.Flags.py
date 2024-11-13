import re

exp = """hello there 
I am from 
Geeks for Geeks"""

print(re.search(r"and", "Sun And Moon", flags=re.IGNORECASE))
print(re.findall(r"^\w", exp, flags = re.MULTILINE))
