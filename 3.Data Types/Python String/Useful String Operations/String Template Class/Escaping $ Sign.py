template = Template('$$ is the symbol for $name')
string = template.substitute(name='Dollar')
print(string)
