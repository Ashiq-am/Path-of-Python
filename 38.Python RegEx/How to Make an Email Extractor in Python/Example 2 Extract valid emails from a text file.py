# importing module
import re

with open('sample.txt', 'r') as file:
    for line in file:
        line = line.strip()

        # finding all valid emails
        reg = re.findall(r"[A-Za-z0-9_%+-.]+"
                         r"@[A-Za-z0-9.-]+ "
                         r"\.[A-Za-z]{2,5}", line)

    # printing all the valid emails found
print(reg)
