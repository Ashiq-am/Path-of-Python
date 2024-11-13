# Plotting superheroes with total superpower
plt.figure(figsize=(12, 6))
Top_ten_total = df.sort_values(by='Total', ascending=False).head(10)
X = Top_ten_total['Name']
Y = Top_ten_total['Total']
plt.xticks(rotation=80)

# plotting line chart
plt.plot(X, Y, 'o-', color='g')
plt.ylabel("Total Superpower", fontsize=18)
plt.xlabel("Superheroes", fontsize=18)
plt.title("Line chart with Total Strength of Superheroes", fontsize=20)
plt.show()
