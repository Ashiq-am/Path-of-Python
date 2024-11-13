fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# First subplot
axs[0].boxplot(data_dict.values(), labels=data_dict.keys())
axs[0].set_title("First Subplot")

# Second subplot
axs[1].boxplot(data_dict.values(), labels=data_dict.keys())
axs[1].set_title("Second Subplot")

plt.show()
