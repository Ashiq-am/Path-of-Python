import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target.reshape(-1, 1) # Reshape to make it a column vector

# One-hot encode the target variable
encoder = OneHotEncoder(categories='auto')
y = encoder.fit_transform(y).toarray()

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 1: Define the model
model = Sequential([
	Dense(10, activation='relu', input_shape=(X_train.shape[1],)),
	Dense(8, activation='relu'),
	Dense(3, activation='softmax')
])
model.summary()
