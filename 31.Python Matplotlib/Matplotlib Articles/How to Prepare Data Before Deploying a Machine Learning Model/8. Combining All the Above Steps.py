# Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import dataset
data = pd.read_csv('datasets/Titanic.csv')

# extract dependent and independent features
x = data.drop('Survived', axis = 1)
y = data['Survived']

# Missing value Imputation
# drop the unrelaven features
x.drop(['Name', 'Ticket', 'Cabin'],
	axis = 1, inplace = True)

# numeric value imputation with mean
x['Age'] = x['Age'].fillna(x['Age'].mean())

# categorical value imputation with mode(most frequent category)
x['Embarked'] = x['Embarked'].fillna(x['Embarked'].mode()[0])

# category encoding
x = pd.get_dummies(x, columns = ['Sex', 'Embarked'],
				prefix = ['Sex', 'Embarked'],
				drop_first = True)

# train-test split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y,
													test_size = 0.2,
													random_state = 0)

# feature scaling
from sklearn.preprocessing import StandardScaler
std_x = StandardScaler()
x_train = std_x.fit_transform(x_train)
x_test = std_x.transform(x_test)
