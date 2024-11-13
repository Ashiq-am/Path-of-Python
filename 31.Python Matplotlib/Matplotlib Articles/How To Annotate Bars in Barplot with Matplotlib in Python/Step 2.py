# Defining the plotsize
plt.figure(figsize=(8, 6))

# Defining the x-axis, the y-axis and the data
# from where the values are to be taken
plots = sns.barplot(x="Name", y="Marks", data=df)

# Setting the x-acis label and its size
plt.xlabel("Students", size=15)

# Setting the y-axis label and its size
plt.ylabel("Marks Secured", size=15)

# Finallt plotting the graph
plt.show()
