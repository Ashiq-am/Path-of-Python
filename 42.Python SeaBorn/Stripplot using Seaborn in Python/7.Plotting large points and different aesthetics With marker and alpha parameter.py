import seaborn
import matplotlib.pyplot as plt

seaborn.set(style='whitegrid')

tips = seaborn.load_dataset("tips")

seaborn.stripplot(x="day", y="total_bill", hue="smoker",
                  data=tips, palette="Set1", size=20,
                  marker="s", alpha=0.2)

plt.show()
