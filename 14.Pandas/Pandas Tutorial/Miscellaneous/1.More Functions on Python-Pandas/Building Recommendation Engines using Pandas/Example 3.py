import matplotlib.pyplot as plt

plt.figure(figsize=(12, 4))
plt.barh(pop_movies['title'].head(6),
		pop_movies['score'].head(6),
		align='center',
		color='RED')

plt.xlabel("Popularity")
plt.title("Popular Movies")
plt.gca().invert_yaxis()
