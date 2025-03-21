# importing library
import matplotlib.pyplot as plt


# function to add value labels
def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i])


if __name__ == '__main__':
    # creating data on which bar chart will be plot
    x = ["Engineering", "Hotel Managment", "MBA",
         "Mass Communication", "BBA", "BSc", "MSc"]
    y = [9330, 4050, 3030, 5500,
         8040, 4560, 6650]

    # making the bar chart on the data
    plt.bar(x, y)

    # calling the function to add value labels
    addlabels(x, y)

    # giving title to the plot
    plt.title("College Admission")

    # giving X and Y labels
    plt.xlabel("Courses")
    plt.ylabel("Number of Admissions")

    # visualizing the plot
    plt.show()
