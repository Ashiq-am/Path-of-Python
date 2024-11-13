# import template
from string import Template

# constructor
myStr = Template("My name is $name and I am $age years old. I am learning $lang")

# safe_substitute method for replacing values
print(myStr.safe_substitute(name="John", lang="Python"))
