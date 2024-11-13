import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'views': [100, 200, 300, 400, 500],
    'likes': [10, 40, 70, 100, 130]
}

# Creating a jointplot
joint_plot = sns.jointplot(x='views', y='likes', data=data)

# Adding the title using plt.suptitle()
plt.suptitle('Views vs Likes - GeeksforGeeks', y=1.02)

plt.show()
