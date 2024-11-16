# Merge based on condition df1['A'] == df2['A']
merge_condition1 = pd.merge(df1, df2, on='A', how='outer')

# Merge based on condition df1['B'] == df2['B']
merge_condition2 = pd.merge(df1, df2, left_on='B', right_on='B', how='outer')

print("Merge based on condition df1['A'] == df2['A']:")
print(merge_condition1)
print("\nMerge based on condition df1['B'] == df2['B']:")
print(merge_condition2)
