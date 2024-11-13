import seaborn
import matplotlib.pyplot as plt

seaborn.set(style='whitegrid')
tip = seaborn.load_dataset("tips")

seaborn.stripplot(x="day", y="total_bill", data=tip)

plt.show()
