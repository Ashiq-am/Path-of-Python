import matplotlib.pyplot as plt

x =['Geeks', 'for', 'geeks', 'tutorials']
y =[1, 2, 3, 4]

# Adding space between label and
# axis by setting labelpad
plt.ylabel('Numbers label', labelpad = 50)

plt.plot(x, y)
