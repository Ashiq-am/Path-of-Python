# Second Linear layer
fc_2 = net.fc2
print('Second Linear Layer :',fc_2)

# APPLY THE Second Linear layer to the output y3
y4 = fc_2(y3)
print('Output Shape :',y4.shape)

# Computational Graph
make_dot(y4, params=dict(fc_2.named_parameters()))
