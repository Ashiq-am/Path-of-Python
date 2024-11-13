# divide the dataset into train and test set
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

df.shape
# o/p: (569, 31)

X_train.shape
# o/p: (398, 30)

X_test.shape
# o/p: (171, 30)

y_train.shape
# o/p: (398,)

y_test.shape
# o/p: (171,)

X_train.head(1)
# will return the top 5 rows (if exists)

ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

X_train
