from sklearn.metrics.cluster import homogeneity_score

# Evaluate the score
hscore = homogeneity_score([0, 0, 1, 1], [0, 1, 2, 3])

print(hscore)
