# Flatten the channels to 1D arrays
R_flatten = R.ravel()
G_flatten = G.ravel()
B_flatten = B.ravel()

# Calculate the correlation matrix
correlation_matrix = np.corrcoef([R_flatten, G_flatten, B_flatten])

print('Correlation Matrix:')
print('   R            G           B')
print(correlation_matrix)

# Visualize the correlation matrix
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.xticks([0, 1, 2], ['R', 'G', 'B'])
plt.yticks([0, 1, 2], ['R', 'G', 'B'])
plt.title('Correlation Matrix')
plt.show()
