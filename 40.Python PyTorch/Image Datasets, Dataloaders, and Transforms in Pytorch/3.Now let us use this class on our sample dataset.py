# Replace the path with the path to your dataset
data_path = './maps/train'

# Creating a dataset object with the path to the dataset
dataset = ImageDataset(data_path)

# Getting the length of the dataset
dataset_length = len(dataset)

# Printing the length of the dataset
print('Number of training examples:',dataset_length)

# Generating a random index within the dataset length
random_index = random.randint(0, dataset_length - 1)

# Plotting the randomly selected image
plt.imshow(dataset[random_index])
plt.show()
