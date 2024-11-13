import matplotlib.pyplot as plt
import seaborn as sns

with sns.axes_style("whitegrid"):
    plt.figure(figsize=(8, 6))
    sns.violinplot(x="day", y="total_bill", data=sns.load_dataset("tips"))
    plt.title("Violin Plot of Total Bill by Day")
    plt.show()
