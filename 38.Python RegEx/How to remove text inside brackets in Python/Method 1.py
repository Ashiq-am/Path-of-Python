# Importing module
import re

# Input string
string="(Geeks)for(Geeks)"

# \(.*?\) ==> it is a regular expression for finding
# the pattern for brackets containing some content
string=re.sub("\(.*?\)","()",string)

# Output string
print(string)
