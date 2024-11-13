# importing packages
import seaborn
import matplotlib.pyplot as plt

############# Main Section ############
# loading dataset using seaborn
df = seaborn.load_dataset('tips')
# pairplot with hue day
seaborn.pairplot(df, hue ='day')
# to show
plt.show()


