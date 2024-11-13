import matplotlib.pyplot as plt

# Visualize the intermediate activations
for layer_name, activation in activations.items():
    print(f'Layer: {layer_name}, Shape: {activation.shape}')
    plt.imshow(activation[0, 0].cpu().numpy(), cmap='gray')
    plt.title(layer_name)
    plt.show()
