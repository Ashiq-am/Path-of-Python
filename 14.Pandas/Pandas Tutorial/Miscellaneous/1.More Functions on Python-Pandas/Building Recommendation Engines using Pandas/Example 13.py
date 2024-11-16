import matplotlib.pyplot as plt

plt.figure(figsize=(12, 4))
plt.barh(corr_Star_Wars_count['title'].head(10),
		abs(corr_Star_Wars_count['Correlation'].head(10)),
		align='center',
		color='red')
plt.xlabel("Popularity")
plt.title("Top 10 Popular Movies")
plt.gca().invert_yaxis()
