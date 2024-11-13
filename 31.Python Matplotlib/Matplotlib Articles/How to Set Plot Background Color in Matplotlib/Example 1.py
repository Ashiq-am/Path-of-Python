# importing library
import matplotlib.pyplot as plt

# giving values for x and y to plot
student_marks = [50, 60, 70, 80, 90]
student_grade = ['B', 'B', 'B+', 'B+', 'A']

plt.plot(student_marks, student_grade)

# Giving x label using xlabel() method
# with bold setting
plt.xlabel("student_marks", fontweight='bold')

# Giving y label using xlabel() method
# with bold setting
plt.ylabel("student_grade", fontweight='bold')

# Giving title to the plot
plt.title("Student Marks v/s Student Grade")

# Showing the plot using plt.show()
plt.show()
