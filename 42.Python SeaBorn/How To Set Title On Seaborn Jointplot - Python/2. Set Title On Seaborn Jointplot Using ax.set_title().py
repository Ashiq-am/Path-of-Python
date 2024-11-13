import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'views': [100, 200, 300, 400, 500],
    'likes': [10, 40, 70, 100, 130]
}

# Creating a jointplot with kind='hex' for hexbin plot behavior
joint_plot = sns.jointplot(x='views', y='likes', data=data, kind='hex')

# Adding the title using ax_joint.set_title() and adjusting the subplot parameters
joint_plot.ax_joint.set_title('Views vs Likes - GeeksforGeeks (Hexbin)', pad=70)

# Adjusting the layout to ensure the title is not overlapped
plt.tight_layout()
plt.subplots_adjust(top=0.9)

plt.show()
