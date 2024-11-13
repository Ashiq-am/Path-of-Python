template = Template( 'That $noun looks ${noun}y')
string = template.substitute(noun='Fish')
print(string)
