import matplotlib.pyplot as plt

# Figure instance with label => lebel
fig = plt.figure( num = 'label' )

fig.get_label()

# This will fetch Figure instace fig only
fig2 = plt.figure( num = 'label' )
assert fig == fig2
