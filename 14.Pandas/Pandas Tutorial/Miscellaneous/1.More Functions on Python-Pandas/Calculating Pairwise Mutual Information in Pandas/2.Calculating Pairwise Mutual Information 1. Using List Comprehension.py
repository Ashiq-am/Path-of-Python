# Function to calculate mutual information between two variables
def calculate_mutual_info(X, y):
    mi = mutual_info_regression(X, y)
    return mi

# Initialize a dictionary to store mutual information values
mutual_info_dict = {}

# Calculate mutual information for each pair of variables
for var1 in independent_vars:
    for var2 in dependent_vars:
        X = data[[var1]]
        y = data[var2]
        mutual_info = calculate_mutual_info(X, y)
        mutual_info_dict[(var1, var2)] = mutual_info[0]  # Get the scalar value

# Convert the dictionary to a DataFrame for easier analysis
mutual_info_df = pd.DataFrame(list(mutual_info_dict.items()), columns=['Variable Pair', 'Mutual Information'])

# Display the results
print(mutual_info_df)
