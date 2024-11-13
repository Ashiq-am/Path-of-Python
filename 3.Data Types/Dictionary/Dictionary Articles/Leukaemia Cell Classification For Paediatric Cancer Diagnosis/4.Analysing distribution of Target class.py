# Data
data = {'HEM - Normal':total_hem_count, 'ALL - Leukemia':total_all_count}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.bar(courses, values, color ='navy')

plt.xlabel("Class")
plt.ylabel("Count")
plt.title("Target Class Distribution")
plt.show()
