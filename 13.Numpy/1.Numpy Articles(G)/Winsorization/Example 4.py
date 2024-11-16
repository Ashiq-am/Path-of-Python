WinsorizedArray = winsorize(array,(0.05,0.05))

plt.boxplot(WinsorizedArray)
plt.title('Winsorized array')
plt.show()
