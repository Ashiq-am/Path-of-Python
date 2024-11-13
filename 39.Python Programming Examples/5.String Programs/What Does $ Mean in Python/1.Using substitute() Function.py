# import Template
from string import Template

# constructor call
myStr = Template("My name is $name and I am learning $lang")

# substitute method for replacing values
print(myStr.substitute(name="John", lang="Python"))
