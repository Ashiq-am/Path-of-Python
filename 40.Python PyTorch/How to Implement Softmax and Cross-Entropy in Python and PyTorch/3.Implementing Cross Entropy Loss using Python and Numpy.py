# The below code implements the cross entropy
# loss between the predicted values and the
# true values of cass labels. The function:
# Inputs: Predicted values, True values
# Output: The cross entropy loss between them.


# Importing the required library
import torch.nn as nn
import torch


# Cross Entropy function.
def cross_entropy(y_pred, y_true):
    # computing softmax values for predicted values
    y_pred = softmax(y_pred)
    loss = 0

    # Doing cross entropy Loss
    for i in range(len(y_pred)):
        # Here, the loss is computed using the
        # above mathematical formulation.
        loss = loss + (-1 * y_true[i] * np.log(y_pred[i]))

    return loss


# y_true: True Probability Distribution
y_true = [1, 0, 0, 0, 0]

# y_pred: Predicted values for each calss
y_pred = [10, 5, 3, 1, 4]

# Calling the cross_entropy function by passing
# the suitable values
cross_entropy_loss = cross_entropy(y_pred, y_true)

print("Cross Entropy Loss: ", cross_entropy_loss)
