# first convolutional layer
conv1 = net.conv1
print('Convulution Layer :',conv1)

# APPLY THE FIRST Convolutional layer to the image
y1 = conv1(img)
print('Output Shape :',y1.shape)

# Computational Graph
make_dot(y1, params=dict(net.named_parameters()))
