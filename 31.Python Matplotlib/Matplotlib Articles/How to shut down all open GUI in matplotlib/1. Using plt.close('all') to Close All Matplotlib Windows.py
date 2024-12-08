import matplotlib.pyplot as plt

fig1 = plt.figure()
fig2 = plt.figure()

plt.plot([1, 2, 3], label='Figure 1')
plt.legend()
plt.figure(fig2.number)
plt.plot([3, 2, 1], label='Figure 2')
plt.legend()

# Close all figures at once
plt.close('all')