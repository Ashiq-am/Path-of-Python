import pandas as pd
import os

directory = 'Data'
all_files = os.listdir(directory)

# Get the full file paths
file_paths = [os.path.join(directory, file) for file in all_files if file.split('.')[-1]=='csv']

# Print the file paths
print('All csv files path:\n',file_paths)
combined_data = pd.concat([pd.read_csv(f) for f in file_paths])
# Reset the index
combined_data.reset_index(inplace=True, drop=True)
# Print the combined DataFrame to the console
print(combined_data)

# Save the combined data to the CSV file
combined_data.to_csv("master_data.csv", index=False)
