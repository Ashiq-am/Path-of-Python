# plotting histogram for knowing the speeds of good superheroes..
plt.figure(figsize=(12, 6))
X = good['Speed']
plt.xticks(np.arange(0, len(X), 5))

# plotting a histogram
plt.hist(X)
plt.title("Distribution of Speed", fontsize=20)
plt.xlabel("Speed", fontsize=18)
plt.ylabel("Number of Super-heroes", fontsize=18)
plt.show()
