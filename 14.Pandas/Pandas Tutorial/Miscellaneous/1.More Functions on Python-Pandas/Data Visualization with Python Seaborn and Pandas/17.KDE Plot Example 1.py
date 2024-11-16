# importing the required libraries
from sklearn import datasets
import pandas as pd
import seaborn as sns

# Setting up the Data Frame
iris = datasets.load_iris()

iris_df = pd.DataFrame(iris.data, columns=['Sepal_Length',
                                           'Sepal_Width', 'Patal_Length', 'Petal_Width'])

iris_df['Target'] = iris.target

iris_df['Target'].replace([0], 'Iris_Setosa', inplace=True)
iris_df['Target'].replace([1], 'Iris_Vercicolor', inplace=True)
iris_df['Target'].replace([2], 'Iris_Virginica', inplace=True)

# Plotting the KDE Plot
sns.kdeplot(iris_df.loc[(iris_df['Target'] == 'Iris_Virginica'),
                        'Sepal_Length'], color='b', shade=True, Label='Iris_Virginica')
