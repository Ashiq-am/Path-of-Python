import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import homogeneity_score


# Changing the location file
# cd C:\Users\Dev\Desktop\Credit Card Fraud

# Loading the data
df = pd.read_csv('creditcard.csv')

# Separating the dependent and independent variables
y = df['Class']
X = df.drop('Class', axis=1)

# Building the clustering model
kmeans = KMeans(n_clusters=2)

# Training the clustering model
kmeans.fit(X)

# Storing the predicted Clustering labels
labels = kmeans.predict(X)

# Evaluating the performance
homogeneity_score(y, labels)
