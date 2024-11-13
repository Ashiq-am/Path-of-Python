# apply Logistic Regression

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(X_train, y_train)

# implemented our model through logistic regression
y_pred = lr.predict(X_test)
y_pred

# array containing the actual output
y_test
