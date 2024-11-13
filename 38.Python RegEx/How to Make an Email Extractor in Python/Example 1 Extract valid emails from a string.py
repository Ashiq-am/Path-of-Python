# Raw text
text = "Duis info@geeksforgeeks.com convallis. " \
       "Parturient montes nascetur ridiculus mus geeksforgeeks@rocks.xyz mauris. " \
       "Odio eu feugiat pre@rsos_tium.index nibh ipsum consequat " \
       "love@gfg.in pretium aenean pharetra magna ac placerat. " \
       "Vitae justo eget magna fermentum iaculis eu non."

#import regex module
import re

#finding all valid emails using regex
reg = re.findall(r"[A-Za-z0-9_%+-.]+"
				r"@[A-Za-z0-9.-]+"
				r"\.[A-Za-z]{2,5}",text)

#printing all the valid emails found
print(reg)
