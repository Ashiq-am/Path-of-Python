WinsorizedArray2 = winsorize(array2,(0.1,0.1))
# In this case, the lower 10% values of
# the data will have their values set equal to the value of the data point at
#the 10th percentile.

plt.boxplot(WinsorizedArray2)
plt.show()

WinsorizedArray2Mean = np.mean(WinsorizedArray2)
