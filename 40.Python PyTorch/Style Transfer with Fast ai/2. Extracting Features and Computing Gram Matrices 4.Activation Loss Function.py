# Define activation loss function
def act_loss(inp: Tensor, targ: Tensor):
    "Calculate the MSE loss of the activation layers"
    return F.mse_loss(inp[-1], targ[-1])
