# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)
# Predict probabilities on the test set
y_pred_proba = model.predict_proba(X_test)[:, 1]
