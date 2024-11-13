# creating a clas
class Program(object):
    language = 'Python'

    # creating a dictionary
    versions = [{'version': '1'}, {'version': '2'}, {'version': '3'}]


# formatting
print('{p.language}: {p.versions[2][version]}'.format(p=Program()))
