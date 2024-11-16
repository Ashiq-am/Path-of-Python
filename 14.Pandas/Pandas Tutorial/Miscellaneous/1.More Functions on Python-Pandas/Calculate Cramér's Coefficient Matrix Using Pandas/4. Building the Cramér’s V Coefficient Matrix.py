# List of categorical variables
categorical_vars = df.columns

# Initialize a DataFrame to store the results
cramers_v_matrix = pd.DataFrame(index=categorical_vars, columns=categorical_vars)

# Calculate Cramér's V for each pair of variables
for var1 in categorical_vars:
    for var2 in categorical_vars:
        cramers_v_matrix.loc[var1, var2] = cramers_v(df[var1], df[var2])

print(cramers_v_matrix)
