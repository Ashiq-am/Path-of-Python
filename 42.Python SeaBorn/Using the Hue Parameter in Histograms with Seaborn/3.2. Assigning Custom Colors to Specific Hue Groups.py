# Define a custom color palette
custom_palette = {
    "Thur - Lunch": "blue",
    "Fri - Lunch": "green",
    "Sat - Dinner": "red",
    "Sun - Dinner": "purple",
    "Thur - Dinner": "cyan",  # Adding missing keys
    "Fri - Dinner": "magenta"  # Adding missing keys
}

# Create a histogram with custom colors
sns.histplot(data=tips, x="total_bill", hue="day_time", palette=custom_palette, multiple="dodge", shrink=0.8)
plt.show()
