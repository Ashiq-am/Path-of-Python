from scipy.stats import entropy
p = [0.4, 0.3, 0.3] # probability distribution
ent = entropy(p, base=2)
print("Entropy:", ent)
