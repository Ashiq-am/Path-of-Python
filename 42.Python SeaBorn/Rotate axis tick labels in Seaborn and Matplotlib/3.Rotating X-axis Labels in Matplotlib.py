import numpy as np
import matplotlib.pyplot as plt

data = {'Cristopher': 20, 'Agara': 15, 'Jayson': 30,
		'Peter': 35}
names = list(data.keys())
age = list(data.values())

fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(names, age, color='blue', width=0.4)

plt.xlabel("Names")
plt.xticks(rotation=45)
plt.ylabel("Age of the person")
plt.show()
