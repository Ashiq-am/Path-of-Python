x = np.arange(0, 10, 1)
print(x)

# X array saved in geekfile.txt
c = np.savetxt("geekfile.txt", x, delimiter =', ')
