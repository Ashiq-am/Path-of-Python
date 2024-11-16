import pandas as pd
# Read the dataset
url= "https://media.geeksforgeeks.org/wp-content/uploads/20240206150437/StudentPerformance.csv"
df = pd.read_csv(url)

# Define the threshold value for "Hours"
threshold = 90 # Replace with your desired threshold
filtered_data = df[df["reading score"] > threshold]

# Print the filtered DataFrame to the console
print(filtered_data)

# Write the filtered data to the target CSV file
filtered_data.to_csv("target.csv", index=False)

print('\n Filtered csv Data copied to target csv files')
