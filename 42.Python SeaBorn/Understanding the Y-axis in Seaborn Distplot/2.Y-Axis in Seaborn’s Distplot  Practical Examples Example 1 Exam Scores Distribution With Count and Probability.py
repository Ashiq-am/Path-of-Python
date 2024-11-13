import seaborn as sns
import matplotlib.pyplot as plt

# Example data: Exam scores of students
exam_scores = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91, 78, 83, 77, 91, 85]

# Create a figure and two subplots
fig, axes = plt.subplots(1, 2, figsize=(10,4))

# Plot histogram with count on the first subplot
sns.histplot(exam_scores, bins=10, kde=False, ax=axes[0])
axes[0].set_xlabel('Scores')
axes[0].set_ylabel('Count')
axes[0].set_title('Exam Scores Distribution (Count)')

# Plot histogram with probability on the second subplot
sns.histplot(exam_scores, bins=10, stat="probability", kde=False, ax=axes[1])
axes[1].set_xlabel('Scores')
axes[1].set_ylabel('Probability')
axes[1].set_title('Exam Scores Distribution (Probability)')

plt.tight_layout()
plt.show()
