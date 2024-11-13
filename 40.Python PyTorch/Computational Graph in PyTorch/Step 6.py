# first Linear layer
fc = net.fc1
print('First Linear Layer :',fc)

# APPLY THE Linear layer to the output y2
y3 = fc(y2)
print('Output Shape :',y3.shape)

# Computational Graph
make_dot(y3, params=dict(net.named_parameters()))
