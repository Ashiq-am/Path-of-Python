plt.figure(figsize=(10, 6))
series.plot(kind='bar', color='coral', width=0.6)
plt.title('Advanced Custom Bar Graph')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.xticks(rotation=30)
plt.grid(True)
plt.show()
