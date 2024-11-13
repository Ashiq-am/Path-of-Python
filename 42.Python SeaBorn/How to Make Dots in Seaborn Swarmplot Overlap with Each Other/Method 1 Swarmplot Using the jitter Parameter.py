# Swarmplot with jitter using stripplot
sns.stripplot(x="day", y="total_bill", data=tips, jitter=True, color="blue", alpha=0.5)  # Adding jittered points
plt.title('Swarmplot with Jitter Using Stripplot')
plt.show()
