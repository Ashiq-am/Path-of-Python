# depict illustration
plt.figure(figsize=(8, 8))
colors_list = ['Red', 'Orange', 'Blue', 'Purple']
graph = plt.bar(data.Format, data.Runs, color=colors_list)
plt.title('Percentage of runs scored by MS Dhoni across all formats')

i = 0
for p in graph:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy()

    plt.text(x + width / 2,
             y + height * 1.01,
             str(data.Percentage[i]) + '%',
             ha='center',
             weight='bold')
    i += 1
plt.show()
