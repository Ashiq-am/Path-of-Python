from string import Template

template = Template('$name is the $job of $company')

string = template.safe_substitute(name='Raju Kumar',
					job='TCE')
print(string)
