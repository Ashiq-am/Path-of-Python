from fitness_tools.composition.bodyfat import JacksonPollock4Site


data = JacksonPollock4Site(20, 'male', (7, 8, 6, 7))

# Calculates bodyfat directly
data.body_fat()
