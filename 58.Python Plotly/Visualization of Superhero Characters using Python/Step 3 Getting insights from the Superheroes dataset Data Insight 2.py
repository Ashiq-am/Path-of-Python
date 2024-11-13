# Top ten good superheroes
good = df[df['Alignment'] == "good"]
Top_ten = good.sort_values(by=['Total'], ascending=False).head(10)
x = Top_ten['Name']
y = Top_ten['Total']

# setting width and height of the figure
plt.figure(figsize=(10, 5))

y_ticks = np.arange(0, y.max()+50, 50)
plt.xticks(rotation=80, fontsize=12)
plt.yticks(y_ticks)

plt.title("Top 10 good super-heroes", fontsize=22)
# plt.grid(visible=None)
plt.bar(x, y, color="g")
plt.show()
