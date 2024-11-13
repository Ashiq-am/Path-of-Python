# Extract nested data using list comprehension
edu_departments = [dept for org in data["organizations"]
				if org["name"] == "GeeksforGeeks" for dept in org["departments"]]
completed_projects = [project for status, projects in data["projects"].items(
) if status == "completed" for project in projects]

print(f"Extracted Data using List Comprehension:")
print(f"Educational Departments: {edu_departments}")
print(f"Completed Projects: {completed_projects}")
