# Top Good Superheroes with both highest strength & Intelligence
X = Max_strength_Intelligence['Name'][0:5]
Intelligence = Max_strength_Intelligence['Intelligence'][0:5]
Strength = Max_strength_Intelligence['Strength'][0:5]

X_axis = np.arange(len(X))
plt.figure(figsize=(10, 5))

# creating bar graph
plt.bar(X_axis - 0.2, Intelligence, 0.4, label='Intelligence')
plt.bar(X_axis + 0.2, Strength, 0.4, label='Strength')

plt.xticks(X_axis, X)
plt.xlabel("Super-heroes", fontsize=18)
plt.ylabel("Strength and Intelligence", fontsize=18)
plt.title("Good Superheroes with highest Strength and Intelligence", fontsize=18)
plt.legend()
plt.show()
