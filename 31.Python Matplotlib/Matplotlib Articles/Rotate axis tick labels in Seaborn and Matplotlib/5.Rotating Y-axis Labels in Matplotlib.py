import numpy as np
import matplotlib.pyplot as plt

data = {'Cristopher': 20, 'Agara': 15, 'Jayson': 30,
		'Peter': 35}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(8, 5))

# creating the bar plot
plt.bar(courses, values, color='blue', width=0.4)
plt.yticks(rotation=45)
plt.xlabel("Names")
plt.ylabel("Age of the person")
plt.show()
