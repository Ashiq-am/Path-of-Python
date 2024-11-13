# Loop through datasets and create plots
for dataset_name, data in datasets.items():
    # Create a new figure for each dataset
    plt.figure(figsize=(8, 6))

    # Generate the histogram plot with KDE (Kernel Density Estimate)
    sns.histplot(data, kde=True)

    # Set the title and labels
    plt.title(f'Distribution of {dataset_name}')
    plt.xlabel('Values')
    plt.ylabel('Frequency')

    # Show the plot grid
    plt.grid(True)

    # Display the plot
    plt.show()
