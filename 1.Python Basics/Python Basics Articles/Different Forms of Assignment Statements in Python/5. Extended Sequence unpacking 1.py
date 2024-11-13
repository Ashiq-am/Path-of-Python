ranks = ['A', 'B', 'C', 'D']
first, *rest = ranks

print("Winner: ", first)
print("Runner ups: ", ', '.join(rest))
