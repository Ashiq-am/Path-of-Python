# importing packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("iris")


def plot():
    sns.lineplot(x="sepal_length", y="sepal_width", data=data)


with sns.axes_style('darkgrid'):
    # Adding the subplot
    plt.subplot(211)
    plot()

plt.subplot(212)
plot()
