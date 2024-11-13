# The below code implements the cross
# entropy loss using the CrossEntropyLoss()
# class provided by torch.nn module in pytorch.


# Importing the required library
import torch.nn as nn
import torch

# Defining the object for this class.
loss = nn.CrossEntropyLoss()

# y_pred: Predicted values
y_pred = torch.tensor([[1.4, 0.4, 1.1, 0.1, 2.3]])

# y_true: True class label
y_true = torch.tensor([0])

# Passing these values to the loss object.
cross_entropy_loss = loss(y_pred, y_true)

# Printing the value of the loss.
print("Cross Entropy Loss: ", cross_entropy_loss.item())
