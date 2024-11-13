def parse(family):
    lastname, *members = family.split()
    return lastname.upper(), *members

print(parse('Charles David John Sam'))
