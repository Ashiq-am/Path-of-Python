def generatorFn():
    data = ["Python", "Java", "C++", "JavaScript", "HTML", "CSS"]

    for language in data:
        yield language


# Using the generator to iterate over the values
for value in generatorFn():
    print(value)
