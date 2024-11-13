# Top Superheroes with Good character who have highest speed and power..
X = Max_Power_Speed['Name'][0:5]
Speed = Max_Power_Speed['Speed'][0:5]
Power = Max_Power_Speed['Power'][0:5]

X_axis = np.arange(len(X))
plt.figure(figsize=(9, 5))

plt.bar(X_axis - 0.2, Speed, 0.4, label='Speed', color='y')
plt.bar(X_axis + 0.2, Power, 0.4, label='Power', color='g')

plt.xticks(X_axis, X)

plt.xlabel("Super-heroes", fontsize=18)
plt.ylabel("Speed and Power", fontsize=18)
plt.title("Good Superheroes with highest Speed and Power", fontsize=18)
plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.show()
