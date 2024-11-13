import matplotlib.pyplot as plt

age = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
cardiac_cases = [5, 15, 20, 40, 55, 55, 70, 80, 90, 95]
survival_chances = [99, 99, 90, 90, 80, 75, 60, 50, 30, 25]

plt.xlabel("Age")
plt.ylabel("Percentage")

plt.plot(age, cardiac_cases, color='black', linewidth=2,
		label="Cardiac Cases", marker='o', markerfacecolor='red', markersize=12)

plt.plot(age, survival_chances, color='yellow', linewidth=3,
		label="Survival Chances", marker='o', markerfacecolor='green', markersize=12)

plt.legend(loc='lower right', ncol=1)
