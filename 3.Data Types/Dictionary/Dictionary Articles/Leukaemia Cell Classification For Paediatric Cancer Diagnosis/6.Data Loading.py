# Initialize lists to store image paths and labels
image_paths = []
image_labels = []

# Iterate through the specified folders
for data_folder_path in [training_all_0, training_all_1, training_all_2, training_hem_0, training_hem_1,
                         training_hem_2]:
    all_images_in_folder = os.listdir(data_folder_path)

    # Determine the label based on the folder name
    image_label = 1 if 'all' in data_folder_path else 0

    # Iterate through images in the folder
    for image_path in all_images_in_folder:
        # Construct the full image path
        full_image_path = os.path.join(data_folder_path, image_path)

        # Append the image path and label to the lists
        image_paths.append(full_image_path)
        image_labels.append(image_label)

# Create a DataFrame from the lists
dict_train = {"image_paths": image_paths, "image_labels": image_labels}
df_train = pd.DataFrame(dict_train)
