# Sample dataset
data = {
    "age_group": ["18-30"] * 50 + ["31-45"] * 50 + ["46-60"] * 50 + ["60+"] * 50,
    "blood_pressure": np.random.normal(120, 15, 50).tolist() +
                      np.random.normal(130, 10, 50).tolist() +
                      np.random.normal(140, 20, 50).tolist() +
                      np.random.normal(150, 25, 50).tolist()
}

df = pd.DataFrame(data)

# Create a violin plot with quartile lines
sns.violinplot(x="age_group", y="blood_pressure", data=df, inner="quartile")
plt.title("Blood Pressure Distribution by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Blood Pressure (mm Hg)")
plt.show()
