# creating a classifier using sklearn
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression(random_state=0, solver='lbfgs',
						max_iter=1000).fit(X_train,
											Y_train)
# printing the acc
clf.score(X_test, Y_test)
