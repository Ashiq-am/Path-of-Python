# Employee DataFrame
employees = {
    'emp_id': [101, 102, 103, 104],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'project_id': [1, 2, 3, 4]
}
df_employees = pd.DataFrame(employees)

# Project DataFrame
projects = {
    'project_id': [3, 4, 5, 6],
    'project_name': ['Project C', 'Project D', 'Project E', 'Project F'],
    'emp_id': [103, 104, 105, 106]
}
df_projects = pd.DataFrame(projects)

print("Employees DataFrame:")
print(df_employees)
print("\nProjects DataFrame:")
print(df_projects)

# Merge based on emp_id
merge_emp_id = pd.merge(df_employees, df_projects, on='emp_id', how='outer')

# Merge based on project_id
merge_project_id = pd.merge(df_employees, df_projects, on='project_id', how='outer')

# Combine and remove duplicates
combined_merge = pd.concat([merge_emp_id, merge_project_id], ignore_index=True)
final_merge = combined_merge.drop_duplicates()

print("\nFinal Merged DataFrame:")
print(final_merge)
