# New titles for the subplots
new_titles = ["New Plot 1", "New Plot 2"]

# Loop through the annotations and update the titles
for i, new_title in enumerate(new_titles):
    fig.layout.annotations[i].text = new_title

# Display the updated figure
fig.show()
